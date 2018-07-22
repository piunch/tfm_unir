####### SECURITY GROUPS #######

resource "aws_security_group" "front_load_balancer_sg" {
  name        = "front_load_balancer_sg"
  description = "Front LoadBalancer Security Group"
  vpc_id      = "${var.vpc_id}"

  # Permitir conexion HTTP
  ingress {
    from_port   = 80
    to_port     = 8080
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 80
    to_port     = 8080
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "back_load_balancer_sg" {
  name        = "back_load_balancer_sg"
  description = "Back LoadBalancer Security Group"
  vpc_id      = "${var.vpc_id}"

  # Permitir conexion HTTP
  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "frontend_sg" {
  name        = "frontend_sg"
  description = "FrontEnd Security Group"
  vpc_id      = "${var.vpc_id}"

  # Permitir conexion ssh
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 22
    to_port     = 22
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Permitir conexion HTTP
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 80
    to_port     = 80
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "backend_sg" {
  name        = "backend_sg"
  description = "BackEnd Security Group"
  vpc_id      = "${var.vpc_id}"

  # Permitir conexion ssh
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 22
    to_port     = 22
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 80
    to_port     = 80
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Permitir conexion HTTP
  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "database_sg" {
  name        = "database_sg"
  description = "Database Security Group"
  vpc_id      = "${var.vpc_id}"

  # Permitir conexion ssh
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 22
    to_port     = 22
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Permitir conexion a la base de datos
  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_subnet" "main_subnet" {
  vpc_id     = "${var.vpc_id}"
  cidr_block = "172.31.16.0/20"

  tags {
    Name = "Main Subnet"
  }
}

####### FRONTEND INSTANCES #######

resource "aws_instance" "frontend_server_1" {
  ami                         = "${var.base_ami_server}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_frontend_key}"
  associate_public_ip_address = "true"
  private_ip                  = "172.31.16.20"
  availability_zone           = "us-east-2c"
  subnet_id                   = "${aws_subnet.main_subnet.id}"

  tags {
    Name = "FrontEnd 1"
  }

  depends_on      = ["aws_security_group.frontend_sg"]
  security_groups = ["${aws_security_group.frontend_sg.id}"]
}

resource "aws_instance" "frontend_server_2" {
  ami                         = "${var.base_ami_server}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_frontend_key}"
  associate_public_ip_address = "true"
  private_ip                  = "172.31.16.21"
  availability_zone           = "us-east-2c"
  subnet_id                   = "${aws_subnet.main_subnet.id}"

  tags {
    Name = "FrontEnd 2"
  }

  depends_on      = ["aws_security_group.frontend_sg"]
  security_groups = ["${aws_security_group.frontend_sg.id}"]
}

####### BACKEND INSTANCES #######

resource "aws_instance" "backend_server_1" {
  ami                         = "${var.base_ami_server}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_backend_key}"
  associate_public_ip_address = "true"
  private_ip                  = "172.31.16.22"
  availability_zone           = "us-east-2c"
  subnet_id                   = "${aws_subnet.main_subnet.id}"

  tags {
    Name = "BackEnd 1"
  }

  depends_on      = ["aws_security_group.backend_sg"]
  security_groups = ["${aws_security_group.backend_sg.id}"]
}

resource "aws_instance" "backend_server_2" {
  ami                         = "${var.base_ami_server}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_backend_key}"
  associate_public_ip_address = "true"
  private_ip                  = "172.31.16.23"
  availability_zone           = "us-east-2c"
  subnet_id                   = "${aws_subnet.main_subnet.id}"

  tags {
    Name = "BackEnd 2"
  }

  depends_on      = ["aws_security_group.backend_sg"]
  security_groups = ["${aws_security_group.backend_sg.id}"]
}

####### DATABASE INSTANCE #######

resource "aws_instance" "database_server" {
  ami                         = "${var.base_ami_server}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_db_key}"
  associate_public_ip_address = "true"
  private_ip                  = "172.31.16.24"
  availability_zone           = "us-east-2c"
  subnet_id                   = "${aws_subnet.main_subnet.id}"

  tags {
    Name = "Database"
  }

  depends_on      = ["aws_security_group.database_sg"]
  security_groups = ["${aws_security_group.database_sg.id}"]
}

resource "aws_elb" "frontend_lb" {
  name               = "frontend-lb"
  availability_zones = ["us-east-2c"]
  subnets            = ["${aws_subnet.main_subnet.id}"]

  listener {
    instance_port     = 8080
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }

  instances                   = ["${aws_instance.frontend_server_1.id}", "${aws_instance.frontend_server_2.id}"]
  cross_zone_load_balancing   = true
  idle_timeout                = 400
  connection_draining         = true
  connection_draining_timeout = 400

  tags {
    Name = "FrontEndLoadBalancer"
  }
}

resource "aws_elb" "backend_lb" {
  name     = "backend-lb"
  internal = true
  subnets  = ["${aws_subnet.main_subnet.id}"]

  listener {
    instance_port     = 8080
    instance_protocol = "http"
    lb_port           = 8080
    lb_protocol       = "http"
  }

  instances                   = ["${aws_instance.backend_server_1.id}", "${aws_instance.backend_server_2.id}"]
  cross_zone_load_balancing   = true
  idle_timeout                = 400
  connection_draining         = true
  connection_draining_timeout = 400

  tags {
    Name = "BackEndLoadBalancer"
  }
}
