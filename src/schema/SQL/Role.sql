


INSERT INTO `audit_srv`.`role` (`name`, `description`, `permissions`) 
VALUES ('Global Admin', 'Can access all audit logs', 'all');

INSERT INTO `audit_srv`.`role` (`name`, `description`, `permissions`) 
VALUES ('Super Admin', 'Can access audit logs of assigned services', 'userSrv,deviceSrv');

INSERT INTO `audit_srv`.`role` (`name`, `description`, `permissions`) 
VALUES ('Service Admin', 'Can access created audit logs', "");
