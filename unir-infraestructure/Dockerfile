FROM hashicorp/terraform:light

COPY variables.tfvars /tmp

ENTRYPOINT  git clone https://github.com/piunch/tfm_unir.git && \
            cd tfm_unir && git checkout develop && \
            mkdir unir-infraestructure/plans && \
            cd unir-infraestructure && terraform init && \
            terraform plan -var-file=/tmp/variables.tfvars -out plans/plan && \
            terraform apply -auto-approve plans/plan