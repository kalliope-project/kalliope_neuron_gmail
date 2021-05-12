# gmail_checker

## Synopsis

This neuron access to Gmail and gives the number of unread mails and their titles.

## Installation
```
kalliope install --git-url https://github.com/kalliope-project/kalliope_neuron_gmail.git
```

## Options

| parameter | required | default | choices | comment    |
|-----------|----------|---------|---------|------------|
| client_secret_file  | YES      |         |         | User credentials |

## Return Values

| Name     | Description                                  | Type | sample                                                       |
|----------|----------------------------------------------|------|--------------------------------------------------------------|
| unread   | Number of unread messages                    | int  | 5                                                            |
| subjects | A List with all the unread messages subjects | list | ['Kalliope commit', 'Beer tonight?', 'cats have superpower'] |

## Synapses example

Simple example : 

```
  - name: "check-email"
    signals:
      - order: "Do I have emails"
    neurons:
      - gmail_checker:
          client_secret_file: "client_secret.json"
          say_template: 
            -  "You have {{ unread }} new emails"    
```

A complex example that read subject emails. This is based on a file_template
```
  - name: "check-email"
    signals:
      - order: "Do I have emails"
    neurons:
      - gmail_checker:
          client_secret_file: "client_secret.json"
          file_template: /templates/my_email_template.j2
```

Here the content of the `my_email_template.j2`
```
You have {{ unread }} email

{% set count = 1 %}
{% if unread > 0 %}
    {% for subject in subjects %}
     email number {{ count }}. {{ subject }}
     {% set count = count + 1 %}
    {% endfor %}
{% endif %}
```
## Notes

You have to generate your credentials like describe here : [https://github.com/jeremyephron/simplegmail#getting-started](https://github.com/jeremyephron/simplegmail#getting-started)


## License

Copyright (c) 2016. All rights reserved.

Kalliope is covered by the MIT license, a permissive free software license that lets you do anything you want with the source code, 
as long as you provide back attribution and ["don't hold you liable"](http://choosealicense.com/). For the full license text see the [LICENSE.md](LICENSE.md) file.
