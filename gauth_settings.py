#coding:utf-8


GA_FILTERS = {
    #sale example
    'sale': 'ga:ProductCategory=~sale',
    'treatment': 'ga:ProductCategory!~sale'
}

GA_ARGS = {
    'client_id': '<your_client_id>.apps.googleusercontent.com',
    'client_secret': '<your_client_secret>',
    'scope':'https://www.googleapis.com/auth/analytics.readonly',
    'user_agent':'<your_user_agent>',
    'ids': 'ga:<your_ga_id>',
    'metrics': 'ga:<metric>',
    'dimensions': 'ga:<dimension>'
}
