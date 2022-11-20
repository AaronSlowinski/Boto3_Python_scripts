import boto3

dynamodb = boto3.resource('dynamodb')

Games=[
        {'Title': "Starcraft", "Genre":"RTS"},
        {'Title': "Starcraft2", "Genre":"RTS"},
        {'Title': "Call of Duty Modern Warfare", "Genre":"FPS"},
        {'Title': "Halo", "Genre":"FPS"},
        {'Title': "Titan Fall", "Genre":"FPS"},
        {'Title': "Unreal Tournament", "Genre":"FPS"},
        {'Title': "Left for Dead 2", "Genre":"FPS"},
        {'Title': "Age of Empires 3", "Genre":"RTS"},
        {'Title': "Portal", "Genre":"FPS"},
        {'Title': "Diablo3", "Genre":"RPG"},

        ]
        
table = dynamodb.Table('Video_Games')
with table.batch_writer() as batch:
    for Title in Games:
        batch.put_item(
            Item=Title
               )