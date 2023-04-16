Add and retrieve todo:
  about: |
    In this story we call the API to buy bread
    and then see that bread is on the list.
  steps:
  - load website
  
  - screenshot

  - enter:
      on: todo text
      text: Add bread

  - click: add

  - should appear:
      text: Add bread
      on: todo list item
      which: first

  - screenshot
