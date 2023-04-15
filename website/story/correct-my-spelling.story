Correct my spelling:
  about: |
    In this story we call the API and send it misspellings.

    The API uses TextBlob (https://textblob.readthedocs.io/en/dev/)
    to detect misspellings and replies to the API with a suggestion
    instead of adding it to the to do list.
  steps:
  - load website
  
  - enter:
      on: todo text
      text: biuy breod

  - click: add

  - should appear:
      text: Did you mean "buy bread"?
      on: error
