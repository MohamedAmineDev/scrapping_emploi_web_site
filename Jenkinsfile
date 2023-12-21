pipeline{
  agent any

  stages{
    stage("Clean un"){
      steps{
        deleteDir()
      }
    }
    stage("Clone repo"){
      steps{
        sh "git clone https://github.com/MohamedAmineDev/scrapping_emploi_web_site.git "
      }
    }
    stage("Generate python application image"){
      steps{
        dir("scrapping_emploi_web_site"){
          sh "docker build -t scrapper1 ."
        }
      }
    }
    stage("Run docker compose"){
      steps{
        dir("scrapping_emploi_web_site"){
          sh "docker compose up -d"
        }
      }
    }
  }
}