-- clong a user 
SELECT groname
FROM pg_user
JOIN pg_group
  ON pg_user.usesysid = ANY(pg_group.grolist)
WHERE usename = 'user1';

-- 

SELECT nspname, relname, relacl
FROM pg_class
JOIN pg_namespace
  ON pg_class.relnamespace = pg_namespace.oid
JOIN pg_user
  ON pg_class.relowner = pg_user.usesysid
WHERE usename = 'user1';

