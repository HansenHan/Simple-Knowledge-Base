Recently, I am seeking jobs through FAS coop. Then, I want to build a KB based on finding a good job. 

My program allows user tell some atoms which not in clauses. Thus, if user want to get the conclusion from rules, he must type the exact atoms in rules. The program will not notice when user type mistakenly.

Here are the rules for finding a good job:
find_good_job <-- high_gpa & good_work_experience & perform_well_in_interview
high_gpa <-- workhard_for_courses & easy_grading
workhard_for_courses <-- do_all_assignments & prepare_all_exams
good_work_experience <-- worked_longtime & relate_to_major
perform_well_in_interview <-- not_nervous_in_interview & high_gpa

Here is an example based on these clauses:
kb> load a4_q2_kb.txt
   5 definite clauses read in:
   find_good_job <-- high_gpa & good_work_experience & perform_well_in_interview
   high_gpa <-- workhard_for_courses & easy_grading
   workhard_for_courses <-- do_all_assignments & prepare_all_exams
   good_work_experience <-- worked_longtime & relate_to_major
   perform_well_in_interview <-- not_nervous_in_interview & high_gpa
kb> tell do_all_assignments prepare_all_exams
  "do_all_assignments" added to KB
  "prepare_all_exams" added to KB
kb> infer_all
  Newly inferred atoms:
     workhard_for_courses
  Atoms already known to be true:
     do_all_assignments, prepare_all_exams
kb> tell easy_grading
  "easy_grading" added to KB
kb> infer_all
  Newly inferred atoms:
     high_gpa
  Atoms already known to be true:
     do_all_assignments, prepare_all_exams, workhard_for_courses, easy_grading
kb> tell worked_longtime relate_to_major
  "worked_longtime" added to KB
  "relate_to_major" added to KB
kb> infer_all
  Newly inferred atoms:
     good_work_experience
  Atoms already known to be true:
     do_all_assignments, prepare_all_exams, workhard_for_courses, easy_grading, high_gpa, worked_longtime, relate_to_major
kb> tell not_nervous_in_interview
  "not_nervous_in_interview" added to KB
kb> infer_all
  Newly inferred atoms:
     perform_well_in_interview find_good_job
  Atoms already known to be true:
     do_all_assignments, prepare_all_exams, workhard_for_courses, easy_grading, high_gpa, worked_longtime, relate_to_major, good_work_experience, not_nervous_in_interview
kb> infer_all
  Newly inferred atoms:
     <none>
  Atoms already known to be true:
     do_all_assignments, prepare_all_exams, workhard_for_courses, easy_grading, high_gpa, worked_longtime, relate_to_major, good_work_experience, not_nervous_in_interview, perform_well_in_interview, find_good_job
kb> Exit
