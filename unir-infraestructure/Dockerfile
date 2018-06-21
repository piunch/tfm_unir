FROM hashicorp/terraform:light

RUN git clone https://github.com/piunch/tfm_unir.git
RUN cd tfm_unir && git checkout develop
RUN cd tfm_unir && mkdir unir-infraestructure/plans

COPY variables.tfvars /tmp

ENTRYPOINT  cd tfm_unir/unir-infraestructure && terraform init && \
            terraform plan -var-file=/tmp/variables.tfvars -out plans/plan && \
            terraform apply -auto-approve plans/plan