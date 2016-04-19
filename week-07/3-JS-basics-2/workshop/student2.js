'use strict';



var dezso = new Student();
dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);
dezso.getCount() // {'rajz': 2, matek: 3}
dezso.getAverage() // 3.4
// szorgalmi
dezso.getAverageBySubject() // {'matek': 4.3, 'rajz': 2}
