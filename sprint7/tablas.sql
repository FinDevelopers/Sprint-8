BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "auditoria_cuenta" (
	"audit_id"	INTEGER,
	"old_id"	INTEGER,
	"new_id"	INTEGER,
	"old_balance"	TEXT,
	"new_balance"	TEXT,
	"old_iban"	TEXT,
	"new_iban"	TEXT,
	"old_type"	TEXT,
	"new_type"	TEXT,
	"user_action"	TEXT,
	"created_at"	datetime,
	PRIMARY KEY("audit_id")
);
CREATE TABLE IF NOT EXISTS "movimientos" (
	"move_id"	INTEGER,
	"account_id"	INTEGER,
	"monto"	INTEGER,
	"tipo_operacion"	TEXT,
	"horario"	datetime,
	PRIMARY KEY("move_id"),
	FOREIGN KEY("account_id") REFERENCES "cuenta"("account_id")
);
INSERT INTO "auditoria_cuenta" VALUES (1,10,10,'9329080','9319080','BH03917052455621804929','BH03917052455621804929','1','1','UPDATE','2022-07-30 19:29:08');
INSERT INTO "auditoria_cuenta" VALUES (2,11,11,'9773274','9763274','MR0825797156643493137017534','MR0825797156643493137017534','1','1','UPDATE','2022-07-30 19:29:08');
INSERT INTO "auditoria_cuenta" VALUES (3,12,12,'-1789861','-1799861','GR8682947553648492174234256','GR8682947553648492174234256','1','1','UPDATE','2022-07-30 19:29:08');
INSERT INTO "auditoria_cuenta" VALUES (4,13,13,'-1672209','-1682209','FR0453741177844280648578404','FR0453741177844280648578404','2','2','UPDATE','2022-07-30 19:29:08');
INSERT INTO "auditoria_cuenta" VALUES (5,14,14,'-6226923','-6236923','ES5263471306788728470322','ES5263471306788728470322','1','1','UPDATE','2022-07-30 19:29:08');
INSERT INTO "auditoria_cuenta" VALUES (6,200,200,'3502069','3402069','FO6225505124074773','FO6225505124074773','1','1','UPDATE','2022-07-30 20:00:17');
INSERT INTO "auditoria_cuenta" VALUES (7,200,200,'3402069','3302069','FO6225505124074773','FO6225505124074773','1','1','UPDATE','2022-07-30 20:03:24');
INSERT INTO "auditoria_cuenta" VALUES (8,200,200,'3302069','3202069','FO6225505124074773','FO6225505124074773','1','1','UPDATE','2022-07-30 20:03:41');
INSERT INTO "auditoria_cuenta" VALUES (9,400,400,'-8076292','-8076292','SM8311798414215862593081646','SM8311798414215862593081646','1','1','UPDATE','2022-07-30 20:03:41');
CREATE VIEW vista as
select customer_id, customer_DNI, customer_name, customer_surname, date('now') - date(dob) as customer_age, branch_number from cliente c inner join sucursal s on s.branch_id = c.branch_id;
CREATE VIEW clientes_por_sucursal as 
select  branch_id, count(customer_id) as total_clientes
from cliente
group by branch_id;
CREATE VIEW empleados_por_sucursal as 
select branch_id, count(employee_id) as total_empleados
from empleado
group by branch_id;
COMMIT;
