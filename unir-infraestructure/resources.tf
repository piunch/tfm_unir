####### SECURITY GROUPS #######

resource "aws_security_group" "load_balancer_sg" {
  name        = "load_balancer_sg"
  description = "LoadBalancer Security Group"

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
}

resource "aws_security_group" "frontend_sg" {
  name        = "frontend_sg"
  description = "FrontEnd Security Group"

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
}

resource "aws_security_group" "backend_sg" {
  name        = "backend_sg"
  description = "BackEnd Security Group"

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

####### FRONTEND INSTANCES #######

resource "aws_instance" "frontend_server_1" {
  ami                         = "${var.base_ami_server}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_frontend_key}"
  associate_public_ip_address = "true"
  availability_zone           = "us-east-2c"

  tags {
    Name = "FrontEnd"
  }

  depends_on      = ["aws_security_group.frontend_sg"]
  security_groups = ["${aws_security_group.frontend_sg.name}"]
}

resource "aws_instance" "frontend_server_2" {
  ami                         = "${var.base_ami_server}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_frontend_key}"
  associate_public_ip_address = "true"
  availability_zone           = "us-east-2c"

  tags {
    Name = "FrontEnd"
  }

  depends_on      = ["aws_security_group.frontend_sg"]
  security_groups = ["${aws_security_group.frontend_sg.name}"]
}

####### BACKEND INSTANCES #######

resource "aws_instance" "backend_server_1" {
  ami                         = "${var.base_ami_database}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_backend_key}"
  associate_public_ip_address = "false"
  availability_zone           = "us-east-2c"

  tags {
    Name = "BackEnd"
  }

  depends_on      = ["aws_security_group.backend_sg"]
  security_groups = ["${aws_security_group.backend_sg.name}"]
}

resource "aws_instance" "backend_server_2" {
  ami                         = "${var.base_ami_database}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_backend_key}"
  associate_public_ip_address = "false"
  availability_zone           = "us-east-2c"

  tags {
    Name = "BackEnd"
  }

  depends_on      = ["aws_security_group.backend_sg"]
  security_groups = ["${aws_security_group.backend_sg.name}"]
}

####### DATABASE INSTANCE #######

resource "aws_instance" "database_server" {
  ami                         = "${var.base_ami_database}"
  instance_type               = "t2.micro"
  key_name                    = "${var.ssh_db_key}"
  associate_public_ip_address = "false"
  availability_zone           = "us-east-2c"

  tags {
    Name = "Database"
  }

  depends_on      = ["aws_security_group.database_sg"]
  security_groups = ["${aws_security_group.database_sg.name}"]
}

resource "aws_elb" "frontend_lb" {
  name               = "frontend-lb"
  availability_zones = ["us-east-2c"]

  listener {
    instance_port     = 80
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
