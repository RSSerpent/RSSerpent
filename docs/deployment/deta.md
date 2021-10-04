# Deploy with Deta.sh

Learn to self-host an RSSerpent instance on [deta.sh](https://www.deta.sh/) (for *free*) through this tutorial.

## Sign Up

In order to deploy on [deta.sh](https://www.deta.sh/), you need to create an account first:

1. Go to <https://web.deta.sh> and register;
2. Fill the *username*, *password* & *email* fields;
3. Confirm the verification email.

If you already have an account, skip this step and sign in.

## Access Token

You will need to create an access token so that RSSerpent could help you do the rest!

1. Go to your home page `https://web.deta.sh/home/{username}/`;
2. Click the *Settings* tab, then click the *Create Token* button;
3. Copy the generated access token to your clipboard.

Read deta's [document](https://docs.deta.sh/docs/cli/auth) if you have any question/concern about the access token.

## Use the Template

RSSerpent provides a [deta.sh](https://www.deta.sh/) deployment template for users. You will need an [GitHub](https://github.com/) account before continuing.

1. Go to the [template](https://github.com/RSSerpent/rsserpent-deploy-deta) on GitHub;
2. Click the green *Use this template* button.

You will be prompted to create a repository based on the template. After successful creation:

1. Go to your repository's *Settings* tab;
2. Go to the *Secrets* section, click the *New repository secret* button;
3. Create a secret whose name is *DETA_TOKEN* and whose value is your [deta.sh](https://www.deta.sh/) access token.

GitHub will need the access token so that it could automatically deploy your RSSerpent instance on [deta.sh](https://www.deta.sh/).

## Add Plugins

The default template doesn't do much. In order to unleash the full power of RSSerpent, you will need to add RSSerpent plugins you need to the `rsserpent.txt` file.

You could clone the repository to edit `rsserpent.txt` locally, or you could just use the GitHub web interface if you are not familiar with git.

Several things to note when writing `rsserpent.txt`:

- It's the same as writing `requirements.txt` for any python project;
- Do not modify `requirements.txt`, only edit `rsserpent.txt`. GitHub Actions will be in charge of automatically updating `requirements.txt` and deploying your instance;
- By *automatically* we mean every week or every time you commit;
- It's recommended to not specify dependency versions so that [GitHub Actions](https://github.com/features/actions) could automatically updates them;

```
# PyPI
rsserpent
# Git
rsserpent-plugin-bilibili @ git+https://github.com/RSSerpent/rsserpent-plugin-bilibili.git
```
- If you do need a specific version of some dependency, you could always pin its version with:

```
# PyPI
rsserpent==0.1.4
# Git
rsserpent-plugin-bilibili @ git+https://github.com/RSSerpent/rsserpent-plugin-bilibili.git@0609c0bd466e5d19fbb13078d9b93e0134b8c5bd
```

## Running 🎉

1. Go to your repository -> *Actions* tab -> *Update* workflow, click the *Run workflow* button to manually trigger a deployment;
2. Go to your [deta.sh](https://www.deta.sh/) home page -> *default* project -> *Micros* tab, select *rsserpent*, you will see the domain name of your instance (usually like *https://xxxxxx.deta.dev/*) at the right-top corner.

Open that domain in your browser. If you see the "Welcome to RSSerpent!" message, congratulations, you are good to go!
