create table users (
	id bigint primary key,
	username varchar(32) default null,
	first_name varchar(64) not null,
	last_name varchar(64) default null,
	is_active bit not null default '1',
	created_at timestamp default now()::timestamp
);

create table contents (
	id int primary key,
	content text not null default 'Сообщение по умолчанию'
);

insert into contents values 
(10000, 'Добро пожаловать в бот с напоминаниями о том, что пора идти в столовую! 
Надеюсь, благодаря ему теперь ни один ужин не будет пропущен...' || chr(10) || chr(10) ||
'Если хочешь получать уведомления, то нажми на кнопку "Хочу получать уведомления" &#128521;'),
(10005, 'Рад тебя видеть! Не пропусти следующий прием пищи! &#127829;'),
(10010, 'Опять пропустил ужин? И куда тебя это привело? Снова ко мне...' || chr(10) || chr(10) ||
'Если хочешь снова получать уведомления, то нажми на кнопку "Хочу получать уведомления" &#128538;'),
(10015, 'Ты уже получаешь уведомления!'),
(10020, 'Супер, теперь ты будешь получать уведомления!' || chr(10) ||
'С понедельника по четверг последний час работы столовки начинается в 17:00, а в пятницу - в 16:00. 
Уведомления будут отправлены в это время и еще каждые 10 минут до закрытия, чтобы ты точно не проворонил ужин &#128540;'),
(10025, 'Ты и так не получаешь уведомления...'),
(10030, 'Ну, как знаешь... Уведомления больше не будут тебе приходить... &#128546;'),
(10035, 'Выберите интересующий вас вопрос: '),
(10040, 'С понедельника по четверг последний час работы столовки начинается в 17:00, а в пятницу - в 16:00. 
Уведомления будут отправлены в это время и еще каждые 10 минут до закрытия, чтобы ты точно не проворонил ужин &#128540;'),
(10045, 'Вы вернулись в главное меню'),
(10050, 'Опять пропустил ужин? И куда тебя это привело? Снова ко мне...' || chr(10) || chr(10) || 
'Теперь ты снова будешь получать уведомления! С понедельника по четверг последний час работы столовки начинается в 17:00, а в пятницу - в 16:00. 
Уведомления будут отправлены в это время и еще каждые 10 минут до закрытия, чтобы ты точно не проворонил ужин &#128540;'),
(10055, '<b>Пора ужинать!</b>' || chr(10) || chr(10) || 
'До закрытия столовки осталось: '),
(10060, '<b>Столовка закрылась...</b>')
