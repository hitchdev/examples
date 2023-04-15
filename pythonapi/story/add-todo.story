Add and retrieve todo:
  about: |
    In this story we call the API to buy bread
    and then see that bread is on the list.
  steps:
  - run:
      code: |
        import todo

        print("Adding an item")
        todo.add_item("buy bread")

        print()
        print("List items:")
        todo.list_items()
      will output: |-
        Adding an item                                                                                                                                                  
        To do added buy bread                                                                                                                                           
                                                                                                                                                                        
        List items:                                                                                                                                                     
        buy bread
