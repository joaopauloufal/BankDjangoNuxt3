#!/bin/bash

chown -R $GID:$UID /usr/src/app
chmod -R 777 /usr/src/app

yarn install
yarn dev -o