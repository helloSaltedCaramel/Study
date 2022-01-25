package com.company;

public class Java100_if_Basic003 {

    public static void main(String[] args) {

        // [1] : 변수 선언
        int kor = 70, eng = 70, math = 50;
        int total_score;
        total_score = kor + eng+ math;

        // [2]: if~ else if ~ else 조건문 사용하기
        if(total_score>=270) {
            System.out.println("당신의 토탈 점수는" +total_score+ "입니다 매우매우 잘했어요.");
            System.out.println("축하해요");
        }else if(total_score >=240) {
            System.out.println("당신의 토탈 점수는" +total_score+ "입니다 잘했어요.");

        } else if(total_score >=210) {
            System.out.println("당신의 토탈 점수는" +total_score+ "입니다 노력하세요.");

        }else{
            if(math >=60)
                System.out.println("당신의 토탈 점수는" + total_score + "입니다 재수강 대상자가 아닙니다.");
            else{
                    System.out.println("당신의 토탈 점수는" + total_score + "입니다 재수강 대상자 입니다.");

            }
        }
    }

}
