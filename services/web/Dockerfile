FROM node
RUN yarn global add serve
WORKDIR /usr/src/app
COPY . .
WORKDIR /usr/src/app/demo
RUN yarn
RUN yarn build
CMD serve -l 3000 -s build
