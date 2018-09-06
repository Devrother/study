# Serverless Framework

~~~
$ sls create -t aws-python3 -p serverless-scrap
~~~
해당 명령어를 통해 serverless freamework 가 aws lambda 템플릿을 만드는 것을 도와준다.

>NOTE <br>
> sls create -t 까지만 입력하면 Supported templates의 목록을 보여준다.

scrap 이라는 디렉토리에 wanted_scrap.py 파일을 생성 후 init_scraping 함수가 포함되어 있는 코드를 작성한 후, 해당 함수를 통해 aws lambda function을 생성해줄 코드를 작성한다. serverless.yml 파일에 작성.

    
~~~ yml
# serverless.yml
functions:
  wanted_scrap:
    handler: scrap/wanted_scrap.init_scraping
    timeout: 300
~~~

serverless.yml 파일을 수정한다. 이 때 runtime 속성을 정확히 해야 오류가 나지 않는다.
~~~ yml
# serverless.yml
provider:
  name: aws
  runtime: python3.6
  stage: dev
  region: ap-northeast-2
~~~
deploy 명령어를 통해 배포한다.
~~~
$ sls deploy
~~~
aws-lambda 콘솔에서 해당 함수의 테스트 실행을 했는데 import 오류가 났다. 찾아보니 serverless-python-requirements 플러그인을 다운받으라 한다.
~~~
$ npm install --save serverless-python-requirements
~~~
serverless.yml 파일을 수정한다.
~~~ yml
# serverless.yml
plugins:
  - serverless-python-requirements
custom:
  pythonRequirements:
    dockerizePip: false
~~~ 
필요한 패키지를 requirements.txt에 명시한다.
~~~ yml
# requirements.txt
requests==2.19.1
~~~
deploy 명령어를 통해 배포했더니, python3 not found 에러가 떴다. 로컬에 설치된 python3는 3.7 버전인데 aws lambda에서 지원하는 버전은 3.6 버전이기 때문이다. 따라서 pyenv와 pyenv-virtualenv를 설치한 후 해당버전의 가상환경에서 deploy 한다.
~~~
$ brew install pyenv
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ source ~/.bash_profile
~~~

> NOTE </br>
> 각자 환경에 맞게 .bash_profile 대신 .bashrc 혹은 .zshrc 로 적용한다.

설치할 수 있는 목록을 확인 후 설치한다.
~~~
$ pyenv install --list
Available versions:
  2.1.3
  2.2.3
  2.3.7
  2.4
  2.4.1
  2.4.2
  2.4.3
  2.4.4
  2.4.5
  2.4.6
...
~~~
~~~
$ pyenv install 3.6.0
~~~
이번엔 python 프로젝트마다 각각의 가상환경을 만들어 줄 수 있는 virtualenv를 설치한다.
~~~
$ brew install pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
~~~

>NOTE <br>
>마찬가지로 .bash_profile 대신 .bashrc 혹은 .zshrc 로 적용한다.

가상환경을 만들고 시작한다.
~~~
$ pyenv virtualenv 2.7.11 {환경명} ## 만들기
$ pyenv activate ## 시작하기
~~~

deploy 명령어를 통해 배포했지만 또 not found 에러가 떳다. pythonBin을 이용하라고 떳다. serverless.yml 파일을 수정한다.
~~~ yml
# serverless.yml
custom:
  pythonRequirements:
    dockerizePip: false
    # pythonBin: /Users/onz/.pyenv/versions/venv/bin/python
~~~
pythonBin 부분을 주석으로 표기한 이유는, 최초 실행시 한번만 실행하면 그 후로는 실행하지 않아도 되는 코드이기 때문이다. 추가 후 deploy 명령어를 통해 배포하고 테스트 실행이 제대로 되는 것을 확인했다.

## ○ 참고문서
* [serverless-python-requirements 활용하기](https://medium.com/@flsqja12_33844/serverless-python-requirements-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0-8c93fdf43c9a)
* [pyenv 및 pyenv-virtualenv 설치하기](https://jiyeonseo.github.io/2016/07/27/install-pyenv/)
* [pyenv로 Python 환경을 macOS에서 간편하고 유연하게 쓰기](https://gist.github.com/perhapsspy/b1d5c175e2c40a1ad21e8e7ec29e8b88)
* [Serverless Python Requirements](https://www.npmjs.com/package/serverless-python-requirements#customize-python-executable)
* [How to Handle your Python packaging in Lambda with Serverless plugins](https://serverless.com/blog/serverless-python-packaging/)
* [Serverless 프레임워크로 서버리스 애플리케이션 생성 및 배포하기](https://velopert.com/3549)