select MOD(10,3)
from dual;

-- 숫자 10을 3으로 나눈 나머지는 ?  == 1 


select empno, MOD(empno, 2)
from emp;

-- 사원 번호가 홀수 이면 1, 짝수이면 0을 출력


select empno, ename
from emp
where MOD(empno, 2) = 0;

-- 짝수인 사원의 사원 번호와 이름을 출력
-- table : emp
