
create table event(event_name TEXT,start_date TEXT,end_date TEXT,venue TEXT,sport TEXT,in_or_out TEXT,description TEXT,event_id varchar(20) NOT NULL,PRIMARY KEY(event_id));
create table enter_team(event_id varchar(10) NOT NULL,team1 varchar(50),team2 varchar(50),FOREIGN KEY(event_id) REFERENCES event(event_id) ON DELETE CASCADE);


create table results(event_name TEXT,winner TEXT,loser TEXT,dept TEXT,cash TEXT);


create table entry(SRN char(13) NOT NULL,in_time datetime,in_out varchar(5),sport varchar(20),guard_name varchar(100),PRIMARY KEY(SRN));

create table coach(SRN char(13),yn varchar(3),coachname varchar(50),sport varchar(50));


DELIMITER $$
create function find_teams(eid varchar(50)) returns int
begin
     declare final int;
     select count(*) into final from enter_team where event_id=eid;
     return final;
    end
$$
DELIMITER ;


DELIMITER $$
create procedure check_date(IN sd date,IN ed date,OUT MSG TEXT)
begin
   if datediff(sd,ed)>0 then
    set MSG='End-date cant be lesser';
    
    end if;
     end
DELIMITER ;

DELIMITER $$
create trigger t3
before insert on entry for each row
    begin
	declare dt datetime;

   	SELECT NOW() INTO dt;
	SET NEW.in_time=dt;
    end
DELIMITER ;

