// DNS del balanceador de carga del frontend
output "front_lb_dns" {
  value = "${aws_elb.frontend_lb.dns_name}"
}

output "back_lb_dns" {
  value = "${aws_elb.backend_lb.dns_name}"
}

output "front1_ip" {
  value = "${aws_instance.frontend_server_1.public_ip}"
}

output "front2_ip" {
  value = "${aws_instance.frontend_server_2.public_ip}"
}

output "back1_ip" {
  value = "${aws_instance.backend_server_1.public_ip}"
}

output "back2_ip" {
  value = "${aws_instance.frontend_server_2.public_ip}"
}

output "db_ip" {
  value = "${aws_instance.database_server.public_ip}"
}
