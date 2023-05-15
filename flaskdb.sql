
drop table if exists Article;

drop table if exists Categorie;

drop table if exists association1;

/*==============================================================*/
/* Table : Article                                              */
/*==============================================================*/
create table Article
(
   id                   int not null,
   nom                  char(25),
   description          char(30),
   prix                 int,
   quantite             int,
   primary key (id),
   key AK_Identifiant_1 (id)
);

/*==============================================================*/
/* Table : Categorie                                            */
/*==============================================================*/
create table Categorie
(
   id                   int not null,
   nom                  char(25),
   primary key (id)
);

/*==============================================================*/
/* Table : association1                                         */
/*==============================================================*/
create table association1
(
   Art_id               int not null,
   id                   int not null,
   primary key (Art_id, id)
);

alter table association1 add constraint FK_association1 foreign key (Art_id)
      references Article (id) on delete restrict on update restrict;

alter table association1 add constraint FK_association1 foreign key (id)
      references Categorie (id) on delete restrict on update 