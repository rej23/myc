provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  
  # count = 2
  ami           = "ami-0c7217cdde317cfec"
  instance_type = "t2.micro"
  key_name      = "firstkey"
  # other instance configurations
  vpc_security_group_ids = ["sg-0a82a67de4707a7e5"]
  tags = {
    Name = "olo"
  }
}

  resource "local_file" "ansible_inventory" {
  content = <<EOF
  all:
    children:
      web:
        hosts: ${aws_instance.example.public_ip}
        vars:
         ansible_user: ubuntu
         ansible_ssh_private_key_file: /home/rej/key.pem
  
  EOF

    filename = "${path.module}/ansible_inventory.yaml"
}

