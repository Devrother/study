FROM mhart/alpine-node:9.7.1

RUN yarn global add nodemon

# 현재 디렉토리의 package.json 파일을 컨테이너의 tmp 폴더 아래에 복사.
COPY ./package.json /tmp/package.json
RUN cd /tmp && yarn install
RUN mkdir -p /usr/src/app && cp -a /tmp/node_modules /usr/src/app

# 작업 디렉토리를 정하여 경로를 고정.
WORKDIR /usr/src/app

COPY ./package.json /usr/src/app
COPY ./src/ /usr/src/app/src/

CMD ["yarn", "start"]