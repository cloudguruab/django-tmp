### Contributing

**commit messages**

```
new - newly implemented user-facing features
chg - changes in existing user-facing features
fix - user-facing bugfixes
oth - other changes which users should know about
dev - any developer-facing changes, regardless of
      new/chg/fix status
```

**heroku**

Check logs for recent change.

```
# web
heroku logs --tail --app loop
```

Dropping into active container

```
heroku run bash -a loop
```

Updating secrets to the cloud container. Please note you should only update `DJANGO_DEBUG=False`, and `SYSTEM_ENV=PRODUCTION` only!

```
$ cat .env | xargs heroku config:set -a loop
```

Pushing to cloud containers.

```
heroku container:push web --app loop
```

Testing local runs for your built container

```
heroku local
```

Making a release once you're local checks out

```
heroku container:release web --app loop
```

Summary, we're deploying our docker container on heroku so we regress to utilizing the heroku Procfile locally for testing. The Procfile includes options you can run before creating a release.

Deploying docker to heroku: https://devcenter.heroku.com/articles/container-registry-and-runtime

Handling Dynos: https://devcenter.heroku.com/articles/one-off-dynos

Error codes: https://devcenter.heroku.com/articles/error-codes
