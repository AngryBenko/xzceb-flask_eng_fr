# coding-project-template

    docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/flask-docker-demo-translator
        docker push us.icr.io/${SN_ICR_NAMESPACE}/flask-docker-demo-translator:latest
            ibmcloud ce application create --name flask-docker-demo-translator --image us.icr.io/${SN_ICR_NAMESPACE}/flask-docker-demo-translator --registry-secret icr-secret
