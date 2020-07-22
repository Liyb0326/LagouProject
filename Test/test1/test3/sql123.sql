begin
for  MYCUR in (select distinct internal_branch,branch_level from tbbranch)
  loop
    for  MYCUR2 in(
      select distinct prd_code
        from tbproduct
       where ta_code = 'ZX'
         and prd_code like '1307%')
      loop
        insert into TBPRDBRANCHALLOW
          (PRD_CODE, INTERNAL_BRANCH, ENABLE_FLAG, RESERVE1)
        values
          (MYCUR2.prd_code, MYCUR.internal_branch, decode(MYCUR.branch_level,1,0,1), ' ');
      END LOOP;
  END LOOP;
end;


select * from  TBPRDBRANCHALLOW


select * from tbtrans where trans_code='100511' for update


select * from tbsequence
