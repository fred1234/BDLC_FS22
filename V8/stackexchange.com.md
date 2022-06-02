# Stackexchange

## Data

https://archive.org/details/stackexchange


## Get unix.stackexchange.com
wget https://archive.org/download/stackexchange/unix.stackexchange.com.7z

## Converter
https://github.com/SkobelevIgor/stackexchange-xml-converter


## not sure
sudo apt install p7zip-full
sudo apt install golang-go


## Schema
https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede


## analzysing 
https://towardsdatascience.com/analyzing-stack-overflow-dataset-with-apache-spark-3-0-39786c141829


## to code






# computing the total number of answers given by the user.

create table project.total_answers as 
SELECT owner_user_id, count(distinct id) as total_answers FROM project.post_answers group by owner_user_id;

# computing the total number correct answers given by the user.

create table project.total_accepted_answers as
SELECT A.owner_user_id as owner_user_id, count(distinct A.id) as total_accepted_answers FROM user_answers.post_answers A,
user_answers.post_questions B
where A.id=B.accepted_answer_id
group by A.owner_user_id;

# number of users
select A.owner_user_id, B.total_accepted_answers, A.total_answers, float(B.total_accepted_answers/A.total_answers)*100  
from total_answers A, total_accepted_answers B 
where A.owner_user_id = B.owner_user_id
LIMIT 10;