# Docker101_3

---

## Dockerfile

---

### 이미지를 생성하는 방법

개발한 어플리케이션을 컨테이너화하려고 하면 떠오르는 방법은 다음과 같다.
1. 텅 빈 이미지(Ubuntu, CentOS 등)로 컨테이너 생성.
2. 애플리케이션을 위한 환경을 설치하고 소스코드 등을 복사해서 동작하는지 확인하는 방법.
3. 컨테이너를 이미지로 commit.

---

![create_image.png](/Users/SeungUk/Documents/devrother-study/presentation/docker/create_image.png)

어플리케이션 설치 & 환경 구축을 하나하나 수작업으로 해야함...

---

Dockerfile 을 이용하여 "이것저것" 등을 기록하여 `build` 명령어를 통해 이미지를 생성할 수 있다.

---

간단한 Dockerfile 을 작성해보자!

---
`Dockerfile` 을 만들자
~~~ shell
$ vi Dockerfile
~~~
~~~ dockerfile
FROM mhart/alpine-node:9.7.1

RUN yarn global add nodemon

# 현재 디렉토리의 package.json 파일을 
# 컨테이너의 tmp 폴더 아래에 복사.
COPY ./package.json /tmp/package.json
RUN cd /tmp && yarn install
RUN mkdir -p /usr/src/app && \
cp -a /tmp/node_modules /usr/src/app

# 작업 디렉토리를 정하여 경로를 고정.
WORKDIR /usr/src/app

COPY ./package.json /usr/src/app
COPY ./src/ /usr/src/app/src/

CMD ["yarn", "start"]
~~~

---

`.dockerignore` 파일을 만들자
~~~shell
$ vi .dockerignore
~~~
~~~
node_modules

yarn-error.log

dist
~~~

---

`package.json` 파일을 만들자
~~~ json
{
    "name": "docker-practice",
    "version": "1.0.0",
    "main": "index.js",
    "license": "MIT",
    "scripts": {
      "start": "nodemon ./src/index.js"
    },
    "dependencies": {
      "express": "^4.16.3",
      "mongoose": "^5.1.1"
    },
    "devDependencies": {
      "nodemon": "^1.17.5"
    }
}

~~~

---

간단한 nodejs server 를 작성하자.

~~~ shell
mkdir src
cd src/
vi index.js
~~~

~~~ js
const express = require('express')
const app = express()
const port = process.env.PORT || 3030

app.use(express.json())

app.listen(port, () => {
    console.log(`listening .. port : ${port}`)
})
~~~

---

이제 `build` 명령어로 이미지를 생성해보자.
~~~ shell
$ docker build . -t docker-practice-server
~~~

---

생성된 이미지로 컨테이너를 실행해보자.

~~~ shell
$ docker run --rm \
--name docker-practice-server \
-p 3030:3030 docker-practice-server
~~~

---

간단한 app 과 Dockerfile 을 작성하고 이미지를 생성하여 컨테이너를 실행해보았다. 

DB(mongodb) 는 어떻게?
DockerHub 에 있는 사용하고자하는 DB 이미지를 받아서 run 하면 된다.
`$ docker run ...`

물론 우리가 띄운 컨테이너와 서로 통신할 수 있게 설정을 해야한다.

---

application 이 커지고 ...
여러 컨테이너(redis, front-server, nginx, 등등) 를 띄워야하는 상황이면?

하나하나 Dockerfile 을 만들고 `run`해서 컨테이너를 실행시켜야하나??

=> NO!

`docker-compose` 를 이용하면 된다!

---

docker-compose 는 다음시간에..
