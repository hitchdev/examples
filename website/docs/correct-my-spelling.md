# Correct my spelling

In this story we call the API and send it misspellings.

The API uses TextBlob (https://textblob.readthedocs.io/en/dev/)
to detect misspellings and replies to the API with a suggestion
instead of adding it to the to do list.


![](https://raw.githubusercontent.com/hitchdev/examples/main/website/screenshots/correct-my-spelling.gif)


* When the website is loaded

![](https://raw.githubusercontent.com/hitchdev/examples/main/website/screenshots/correct-my-spelling-1-screenshot.png)

* Enter text `biuy breod` on `todo text`.

* Click on `add`.


* Then text `Did you mean "buy bread"?` should appear on `error`.


![](https://raw.githubusercontent.com/hitchdev/examples/main/website/screenshots/correct-my-spelling-5-screenshot.png)
