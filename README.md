#constant-demo#


#Steps taken#

##Setup Project##

###API###

mkdir api
cd api
python3 -m venv venv
source venv/bin/activate
pip install Flask
pip freeze > requirements.txt
deactivate

###WEB###
npx create-react-app web --template cra-template-pwa
cd web
rm package-lock.json
rm -Rf node_modules
vi package.json (change react-router-dom to "5" to get Switch)
yarn

###DB###
mkdir db
cd db
vi create_tables.sh
vi insert_demo_data.sh

###OPS###
mkdir ops
cd ops
mkdir docker
cd docker
vi Dockerfile.db
vi Dockerfile.web
vi Dockerfile.api
vi .dockerignore
vi docker-compose.yml
cd ../
mkdir conf
cd conf
vi nginx.conf

###GENERAL###
vi build_docker.sh
vi start_docker.sh
vi .gitignore
git status
git add .
git commit -m "initial setup of constant demo with docker config"


##Development##

###WEB###
cd web
yarn add react-router-dom
yarn add node-sass
mkdir src/components
mkdir src/assets
mkdir src/pages
mkdir src/components/header
mkdir src/components/menu
mkdir src/components/loan-list
mkdir src/pages/homepage
code . (invoke visual studio code)
create file src/components/header/header.component.jsx
create file src/components/header/header.styles.scss
create file src/components/menu/menu.component.jsx
create file src/components/menu/menu.styles.scss
create file src/components/loan-list/loan-list.component.jsx
create file src/components/loan-list/loan-list.styles.scss
create file src/pages/homepage/homepage.component.jsx
create file src/pages/homepage/homepage.styles.scss
modify src/App.js to include homepage component

