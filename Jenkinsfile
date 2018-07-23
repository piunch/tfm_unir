node {
    wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'xterm']) {
        
        /// STAGE CLEANUP

        stage('Clean docker images, networks and containers') {
            sh 'rm -rf unir-infraestrucure'
            sh 'docker container ls -a -q'
            sh 'if [ -n "$(docker container ls -a -q)" ]; then docker container rm -v -f $(docker container ls -a -q); fi'
            sh 'if [ -n "$(docker images unir/bd -q)" ]; then docker rmi -f $(docker images unir/bd -q); fi'
            sh 'if [ -n "$(docker images unir/backend -q)" ]; then docker rmi -f $(docker images unir/backend -q); fi'
            sh 'if [ -n "$(docker network ls | grep testnet)" ]; then docker network rm testnet; fi'
        }

        /// STAGE CLONE REPO

        stage('Clone Repo') {
            git url: 'https://github.com/piunch/tfm_unir.git', branch: 'develop'
            sh 'ls unir-backend/'
        }

        /// STAGE BUILD

        stage('Build docker images') {
            withCredentials([string(credentialsId: 'BD_USER_TEST', variable: 'BD_USER_TEST'), 
                                string(credentialsId: 'BD_PASSWORD_TEST', variable: 'BD_PASSWORD_TEST'),
                                string(credentialsId: 'MYSQL_ROOT_PASS_TEST', variable: 'MYSQL_ROOT_PASS_TEST')]) {
                def bdImage    = docker.build("unir/bd", "--build-arg MYSQL_USER=$BD_USER_TEST --build-arg MYSQL_PASSWORD=$BD_PASSWORD_TEST --build-arg MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASS_TEST -f unir-bd/Dockerfile unir-bd/")
                def backImage  = docker.build("unir/back", " -f unir-backend/Dockerfile unir-backend/")
            }
        }
        
        /// STAGE CREATE DOCKER SUBNET

        stage('Create docker subnet') {
            sh 'docker network create --subnet=172.18.0.0/16 testnet'
        }

        /// STAGE RUN CONTAINERS

        stage('Run Containers') {
            withCredentials([string(credentialsId: 'IP_HOST_BD_TEST', variable: 'IP_HOST_BD_TEST')]) {
                sh 'docker run --name unir-bd -e TEST=true --net testnet --ip $IP_HOST_BD_TEST -dt unir/bd'
            }

            sh 'sleep 6'

            withCredentials([string(credentialsId: 'BD_USER_TEST', variable: 'BD_USER_TEST'), 
                            string(credentialsId: 'BD_PASSWORD_TEST', variable: 'BD_PASSWORD_TEST'),
                            string(credentialsId: 'TOKEN_KEY_TEST', variable: 'TOKEN_KEY_TEST'),
                            string(credentialsId: 'IP_HOST_BD_TEST', variable: 'IP_HOST_BD_TEST')]) {
                sh 'docker run --name unir-back -e TOKEN_KEY=$TOKEN_KEY_TEST -e BD_NAME=TFMUNIRBD -e BD_USER=$BD_USER_TEST -e BD_PASSWORD=$BD_PASSWORD_TEST -e BD_HOST=$IP_HOST_BD_TEST --net testnet --ip 172.18.0.3 -d unir/back'
            }
        }
        
        /// STAGE RUN TESTS
        
        stage('Run Tests') {
            sh 'docker exec -i unir-back pip3 install --no-cache-dir -r test-requirements.txt'
            sh 'docker exec -i unir-back mkdir -p /usr/test/'
            sh 'rm -f /usr/test/test_report.xml'
            try {
                sh 'docker exec -i unir-back pytest --junitxml=/usr/test/test_report.xml'
            } catch(e) {
                sh 'docker exec -i unir-back cat /usr/test/test_report.xml > test_report.xml'
                junit 'test_report.xml'
                sh 'exit 1'
            }
            sh 'docker exec -i unir-back cat /usr/test/test_report.xml > test_report.xml'
            junit 'test_report.xml'
        }
        
        /// STAGE DEPLOYMENT
        
        stage('Deployment') {
            dir("unir-infraestructure") {
                sh 'mkdir -p plans'
                sh 'terraform init -input=false'
                withCredentials([string(credentialsId: 'AWS_SECRET', variable: 'AWS_SECRET_ACCESS_KEY'), 
                            string(credentialsId: 'AWS_ACCESS_KEY', variable: 'AWS_ACCESS_KEY_ID'),
                            string(credentialsId: 'AWS_DEFAULT_REGION', variable: 'AWS_DEFAULT_REGION')]) {
                    sh 'terraform plan -var-file=config/dev.tfvars -out=plans/plan -input=false'
                    sh 'terraform apply -input=false plans/plan'
                    sh 'sleep 6'
                }

                // Variables de salida
                frontendLoadBalancer = sh(returnStdout: true, script: "terraform output front_lb_dns").trim()
                backendLoadBalancer  = sh(returnStdout: true, script: "terraform output back_lb_dns").trim()
                backend1_ip          = sh(returnStdout: true, script: "terraform output back1_ip").trim()
                backend2_ip          = sh(returnStdout: true, script: "terraform output back2_ip").trim()
                frontend1_ip         = sh(returnStdout: true, script: "terraform output front1_ip").trim()
                frontend2_ip         = sh(returnStdout: true, script: "terraform output front2_ip").trim()
                database_ip          = sh(returnStdout: true, script: "terraform output db_ip").trim()
            }
            sh 'tar cvzf terraformState.tar.gz unir-infraestructure'
            archiveArtifacts artifacts: 'terraformState.tar.gz'

            withCredentials([string(credentialsId: 'BD_USER_PRO', variable: 'BD_USER_PRO'), 
                            string(credentialsId: 'BD_PASSWORD_PRO', variable: 'BD_PASSWORD_PRO'),
                            string(credentialsId: 'MYSQL_ROOT_PASS_PRO', variable: 'MYSQL_ROOT_PASS_PRO')]) {
                def database = docker.build("unir/bd", "--build-arg MYSQL_USER=$BD_USER_PRO --build-arg MYSQL_PASSWORD=$BD_PASSWORD_PRO --build-arg MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASS_PRO -f unir-bd/Dockerfile unir-bd/")
                def backend  = docker.build("unir/back", " -f unir-backend/Dockerfile unir-backend/")
                def frontend = docker.build("unir/front", " -f unir-frontend/TFMfront/Dockerfile unir-frontend/TFMfront/")
            }

            dir('unir-deployment') {
                sh 'docker save --output unir-frontend.tar unir/front'
                sh 'docker save --output unir-database.tar unir/bd'
                sh 'docker save --output unir-backend.tar unir/back'
                
                sh 'rm -f /var/lib/jenkins/.ssh/known_hosts'
                withCredentials([string(credentialsId: 'BD_USER_PRO', variable: 'BD_USER_PRO'), 
                                string(credentialsId: 'BD_PASSWORD_PRO', variable: 'BD_PASSWORD_PRO'),
                                string(credentialsId: 'TOKEN_KEY_PRO', variable: 'TOKEN_KEY_PRO'),
                                string(credentialsId: 'IP_HOST_BD_PRO', variable: 'IP_HOST_BD_PRO')]) {
                    // Frontend Playbook
                    sh "ansible-playbook -i inventory.ini --extra-vars  \"{\\\"pro_host\\\":\\\"$backendLoadBalancer\\\"}\" frontend-playbook.yml"
                    // Backend Playbook
                    sh "ansible-playbook -i inventory.ini backend-playbook.yml"
                    // Database Playbook
                    sh "ansible-playbook -i inventory.ini database-playbook.yml"
                } 
            }
        }
        
        /// STAGE ARCHIVE ARTIFACTS & CLEANUP

        stage('Archive artifacts') {
            dir('unir-deployment') {
                sh 'gzip -f unir-frontend.tar'
                sh 'gzip -f unir-backend.tar'
                sh 'gzip -f unir-database.tar'
                archiveArtifacts artifacts: '*.tar.gz'
            }
            // Se borran los contenedores e imagenes
            
            sh 'docker container ls -a -q'
            sh 'if [ -n "$(docker container ls -a -q)" ]; then docker container rm -v -f $(docker container ls -a -q); fi'
            sh 'if [ -n "$(docker images unir/bd -q)" ]; then docker rmi -f $(docker images unir/bd -q); fi'
            sh 'if [ -n "$(docker images unir/backend -q)" ]; then docker rmi -f $(docker images unir/backend -q); fi'
            sh 'if [ -n "$(docker network ls | grep testnet)" ]; then docker network rm testnet; fi'
            sh 'if [ -n "$(docker volume ls -q)" ]; then docker volume rm $(docker volume ls -q); fi'
        }
        
        echo "FRONTEND DNS: $frontendLoadBalancer"
    }
}
