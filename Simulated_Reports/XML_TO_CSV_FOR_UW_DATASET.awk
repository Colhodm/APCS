 #BreastDensity: Almost_Entirely_Fat, Scattered_Fibroglandular_Densities, Hetero genously_Dense, Extremely_Dense, Not_Specified
# MassesMargins: Circumscribed, Illdefined, CannotDiscern, Spiculated, Microlobu
#lated
# MassesShape: Oval, Round, Irregular, Loblar, CannotDiscern
# MassesDensity: Equal, CannotDiscern, High, Low. Fatdensity
# MassesSize: Small, Large
# BIRADS_category: 0-5

BEGIN {
calGrouped = "*";
calClustered = "*";
calScattered = "*";
calRegional = "*";
calDiffuse = "*";
calSingle = "*";
calSegmental = "*";
Ctype = "*";
Distribution_Type = 0;
abnormality_scope = 0;
calSuture = "None";
#calDermal = "None";
calskin = "None";
calPleomorph = "None";
calRod = "None";
calCoarseHetero = "None";
calMilkof = "None";
calDystro = "None";
calRim = "None";
calAmorphous = "None";
calCoarse = "None";
calEggshell = "None";
calVasc = "None";
calPunctate = "None";
calLucent = "None";
calLinear = "None";
stability123 = "*";
tumorgrowth = "*";
surgeryhx = "*";
familyhx = "*";
extraneous_info = "*";
Lesion_type = "*";
Lesion_properties = "*";
CalcificationType = "*";
Calcification = "*"; 
total_records = 0;
breastDensity = "*";
birads_category = "*";
masses_shape = "*";
masses_margin = "*";
masses_density = "*";
size = "*";
lesion_type = "*";
diagnosis = "*";
Birads_score = "*";
hormone_treatment = "*";
age = "*";
BreastHX = "*";

Trabecular_Thickening  = "None";
Axillary_Adenopathy  = "None";
Architectual_Distortion = "None";
Nipple_Retraction  = "None";
Skin_Retraction  = "None";
Skin_Thickening  = "None";

#print "diagnosis, " "birads_category, " "breastDensity, " "masses_shape, " "masses_margin, " "masses_density," "lesion_type , " "hormone_treatment," "Stability," "tumorgrowth," "surgeryhx," "familyhx, " "BreastHX, " "age," " Trabecular_Thickening, " " Axillary_Adenopathy,  " " Architectual_Distortion, " " Nipple_Retraction, " " Skin_Retraction, " "Skin_Thickening, " "CalSuture, " "calDermal, " "calskin, " "calPleomorph, " "calRod, " "calCoarseHetero, " " calMilkof, " "calDystro, " "calRim, " "calAmorphous," "calCoarse," "calEggshell," "calVasc," "calPunctate," "calLucent," "calLinear, " " size, """ ; 
}
#New Added Fields
/The Family History of the Patient is None/{familyhx = "None";}
/The Family History of the Patient is Minor/{familyhx = "Minor";}
/The Family History of the Patient is Strong/{familyhx = "Strong";}
/The History of Surgery is NoSurgery/{surgeryhx = "None";}
/The History of Surgery is PriorSurgery/{surgeryhx = "Prior";}
/The Growth of the Tumor is Benign/{tumorgrowth = "Benign";}
/The Growth of the Tumor is Invasive./{tumorgrowth = "Invasive";}
/The Growth of the Tumor is InSitu./{tumorgrowth = "InSitu";}
/The Masses Stability is Stable/{stability123 = "Stable";}
/The Masses Stability is Increasing/{stability123 = "Increasing";}
/The Masses Stability is Decreasing/{stability123 = "Decreasing";}
#Calcification
#/Milk_of_Calcium/ {calMilkof =Calcification;}
#/coarse/ {calCoarse = Calcification;}
#/Coarse/ {calCoarse = Calcification;}
#/vascular/ {calVasc = Calcification;}
#/Vascular/ {calVasc= Calcification;}
#/eggshell/ {calEggshell= Calcification;}
#/Eggshell/ {calEggshell = Calcification;}
#/popcorn/ {calCoarse = Calcification;}
#/Popcorn/ {calCoarse = Calcification;}
#/dystrophic/ {calDystro= Calcification;}
#/Dystrophic/ {calDystro= Calcification;}
#/lucent/ {calLucent = Calcification;}
#/Lucent/ {calLucent = Calcification;}
#/rodlike/ {calRod= Calcification;}
#/Rodlike/ {calRod = Calcification;}
#/suture/ {calSuture = Calcification;}
#/Suture/ {calSuture= Calcification;}
#/dermal/ {calDermal = Calcification;}
#/Dermal/ {calDermal= Calcification;}
#/Rim/ {calRim = Calcification;}
#/rim/ {calRim = Calcification;}
#/punctate/ {calPunctate = Calcification;}
#/Punctate/ {calPunctate = Calcification;}
#/punctuate/ {calPunctate = Calcification; }
#/Punctuate/ {calPunctate= Calcification; }
#/pleomorphic/ {calPleomorph= Calcification;}
#/Pleomorphic/ {calPleomorph = Calcification;}
#Fine Linear/ {calPleomorph = Calcification;}
#/fine linear/ {calPleomorph = Calcification;}
#/Coarse_Heterogeneous/ {calCoarseHetero = Calcification};
#/amorphous/ {calAmorphous = Calcification;}
#/Amorphous/ {calAmorphous= Calcification;}


#Age
#i#.The Age of Patient is The Age is 65 - 70
/The Age of Patient is The Age is 51 - 54./ {age = "51-54";}
/The Age of Patient is The Age is 55 - 60./ {age = "55-60";}
/The Age of Patient is The Age is 61 - 64./ {age = "61-64";}
/The Age of Patient is The Age is 45 - 50./ {age = "45-50";}
/The Age of Patient is The Age is 40 - 44./ {age = "40-44";}
/The Age of Patient is The Age is 65 - 70./ {age = "65-70";}

#Hormone History
/The History of Hormone Treatment is LessThan5Yr./ {hormone_treatment = "Less_than_5_years";}
/The History of Hormone Treatment is None./ {hormone_treatment = "None"; }
/The History of Hormone Treatment is MoreThan5Yr./ {hormone_treatment = "More_Than_5_years"; }
/The History of Breast Cancer is NoHxBreastCA./ {BreastHX = "None"; }
/The History of Breast Cancer is HxDCorLC./ {BreastHX = "Present"; }
/The Diagonsis is Benign./ {diagnosis = "Benign"; }
/The Diagonsis is Malignant./ {diagnosis = "Malignant"; }
/BI-RADS 1/ {Birads_score = 1; }
/BI-RADS 0/ {Birads_score = 0; }
/BIRADS 0/ {Birads_score = 0; }
/BIRADS 1/ {Birads_score = 1; }
/BI-RADS 5/ {Birads_score = 5; }
/BIRADS 5/ {Birads_score = 5; }

/BIRADS 2/ {Birads_score = 2; }
/BI-RADS 2/ {Birads_score = 2; }

/BIRADS 3/ {Birads_score = 3; }
/BI-RADS 3/ {Birads_score = 3; }

/BIRADS 3-./ {Birads_score = 3; }
/BI-RADS 4/ {Birads_score = 4; } 
/BIRADS 4/ {Birads_score = 4; }
/The Birads Score is 5./ {Birads_score = 5; }
#/The History of Hormone Treatment is/ {print NF " 3"}
#/The Age of Patient is/ { print NF " 4"}

/Case breastDensity/ {
split($2, array,"\""); 
#print "BreastDensity " array[2];

if (array[2] == "Almost_Entirely_Fat") {
breastDensity = "Class1";
}
else if (array[2] == "Scattered_Fibroglandular_Densities") {
breastDensity = "Class2";
}
else if (array[2] == "Heterogeneously_Dense") {
breastDensity = "Class3";
}
else if (array[2] == "Extremely_Dense") {
breastDensity = "Class4";
}
else if (array[2] == "Not_Specified") {
breastDensity = "*";
}
#print array[2]"   "breastDensity;
}
/<Text value = "BIRADS 0/ {
	birads_category =  "working"; 
#print "birads_category "  birads_category;
}
/MAMMOGRAPHY IMPRESSION:ADDITIONAL EVALUATION RECOMMENDED/ {
	birads_category =  "0"; 
        lesion_type = "UNKNOWN";
#   	print "birads_category "  birads_category;
}
/<Text value="BI-RADS 0/ {
	birads_category =  "poop"; 
        lesion_type = "UNKNOWN";
#   	print "birads_category "  birads_category;
}
/<Text value = "BI-RADS 1/ {
	birads_category =  "1"; 
        lesion_type = "BENIGN";
#   	print "birads_category "  birads_category;
}
/<Text value = "BI-RADS 2/ {
	birads_category =  "2"; 
        lesion_type = "BENIGN";
#   	print "birads_category "  birads_category;
}
/BIRADS 3-/ {
	birads_category =  "3"; 
        lesion_type = "BENIGN";
#   	print "birads_category "  birads_category;
}
/<Text value="BENIGN MAMMOGRAM/ {
	birads_category =  "2"; 
        lesion_type = "BENIGN";
#   	print "birads_category "  birads_category;
}
/BIRADS 4/ {
	birads_category =  "4"; 
        lesion_type = "MALIGNANT";
#   	print "birads_category "  birads_category;
}
/<Text value="SUSPICIOUS / {
	birads_category =  "4"; 
        lesion_type = "MALIGNANT";
#   	print "birads_category "  birads_category;
}
/SUSPICIOUS OF MALIGNANCY/ {
	birads_category =  "4"; 
        lesion_type = "MALIGNANT";
#   	print "birads_category "  birads_category;
}
/<Text value="BI-RADS 1:/ {
	birads_category =  "1"; 
        lesion_type = "BENIGN";
#   	print "birads_category "  birads_category;
}
/BIRADS 5/ {
	birads_category =  "5"; 
        lesion_type = "MALIGNANT";
#   	print "birads_category "  birads_category;
}
/<Text value="HIGHLY SUGGESTIVE OF MALIGNANCY/ {
	birads_category =  "5"; 
        lesion_type = "MALIGNANT";
#   	print "birads_category "  birads_category;
}

/<Abnormality/ {abnormality_scope = 1; if ($5 == "type=\"Calcification\">") {
Distribution_Type = 0;
Ctype = "*";
calc_scope = 1; 
calSuture = "None";
calDermal = "None";
calskin = "None";
calPleomorph = "None";
calRod = "None";
calCoarseHetero = "None";
calMilkof = "None";
calDystro = "None";
calRim = "None";
calAmorphous = "None";
calCoarse = "None";
calEggshell = "None";
calVasc = "None";
calPunctate = "None";
calLucent = "None";
Calcification = "*"; 
#print;
}
}


/<\/Abnormality/ {
abnormality_scope = 0;  
if (calc_scope == 1) {	
	calc_scope = 0;
        if (Distribution_Type == 0) {  # Distribution was not found
               # print "HERE   "  Ctype;
		Calcification = "Present";

		if (Ctype == "Fine_Linear") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2];
                        calLinear = Calcification;
                }
                if (Ctype == "Fine_Linear_Branching") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                        calLinear = Calcification;

                }
                if (Ctype == "Punctate") {
                #       print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                        calPunctate = Calcification;
                }
	 	if (Ctype == "Vascular") {
                      	 #print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
			calVasc = Calcification
                }
                if (Ctype == "Skin") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                        calskin = Calcification;
                }
                if (Ctype == "Amorphous") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2];
                        calAmorphous = Calcification;
                }
                if (Ctype == "Large_Rod_Like") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                        calRod = Calcification;
                }
                if (Ctype == "Lucent_Centered") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                        calLucent = Calcification;
                }
                if (Ctype == "Dystrophic") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                        calDystro = Calcification;
                }
                if (Ctype == "Fine_Pleomorphic") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                        calPleomorph = Calcification;
                #	print "HERE2   "  calPleomorph;
                }
                if (Ctype == "Eggshell") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                        calEggshell = Calcification;
                }
                if (Ctype == "Rim") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                        calRim = Calcification;
                }
                if (CType == "Coarse") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2];
                        calCoarse = Calcification;
                }
                if (CType == "Coarse_Heterogeneous") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2];
                        calCoarseHetero = Calcification;
                }
                if (Ctype == "Milk_of_Calcium") {
                        #print "Calcification  = " CalcificationType "Array 2 = " array[2];
                        calMilkof = Calcification;
                }
   		 if (Calcification == "Grouped"){
                        calGrouped = Calcification;
                }
                if (Calcification == "Clustered"){
                        calClustered = Calcification;
                }

                if (Calcification == "Scattered"){
                        calScattered = Calcification;
                }
                if (Calcification == "Regional"){
                        calRegional = Calcification;
                }
                if (Calcification == "Diffuse"){
                        calDiffuse = Calcification;
                }
                if (Calcification == "Single"){
                        calSingle = Calcification;
                }
                if (Calcification == "Segmental"){
                        calSegmental = Calcification;
                }
	}
}
}

/Descriptor type/{ 
if ($2 ~ /Category/) {
	split($3, array,"\""); 
# 	print "Category " array[2];
#  lesion_type = array[2];
}
if ($2 ~ /Shape/) {
	split($3, array,"\""); 
#	print FILENAME"  " "*****Shape  " array[2];
	masses_shape = array[2];
}
if ($2 ~ /Margin/) {
	split($3, array,"\""); 
	masses_margin =  array[2];
        if (masses_margin == "Obscured")
		masses_margin = "CannotDiscern";
        else if (masses_margin == "Indistinct") 
		masses_margin = "CannotDiscern";
}
if ($2 ~ /Density/) {
	split($3, array,"\""); 
#	print "MassesDensity    " array[2];
	masses_density =  array[2];
        if (masses_density == "Fat_Containing")
		masses_density = Fatdensity;
}
if ($2 ~ /Distribution/) {
	split($3, array,"\"");
        if (calc_scope == 1) {
              Distribution_Type = 1; # Found a Distribution Attribute
	      Calcification = array[2];
		#print array[2];
		#print "YAWN";
        	if (Ctype == "Fine_Linear") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2];
               		calLinear = Calcification;
		}
        	if (Ctype == "Fine_Linear_Branching") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
			calLinear = Calcification;
		}
        	if (Ctype == "Punctate") {
        	#	print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
               		calPunctate = Calcification;
        	}
        	if (Ctype == "Vascular") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
			calcVasc = Calcification;
		}
        	if (Ctype == "Skin") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
               		calskin = Calcification;
        	}
        	if (Ctype == "Amorphous") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2];
               		calAmorphous = Calcification; 
        	}
        	if (Ctype == "Large_Rod_Like") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
               		calRod = Calcification;
        	}
        	if (Ctype == "Lucent_Centered") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
               		calLucent = Calcification;
        	}
        	if (Ctype == "Dystrophic") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
               		calDystro = Calcification;
        	}
        	if (Ctype == "Fine_Pleomorphic") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                	calPleomorph = Calcification;
        	}
        	if (Ctype == "Eggshell") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                	calEggshell = Calcification;
        	}
        	if (Ctype == "Rim") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2]; 
                	calRim = Calcification;
        	}
        	if (CType == "Coarse") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2];
                	calCoarse = Calcification; 
        	}
        	if (CType == "Coarse_Heterogeneous") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2];
                	calCoarseHetero = Calcification; 
        	}
        	if (Ctype == "Milk_of_Calcium") {
        		#print "Calcification  = " CalcificationType "Array 2 = " array[2];
                	calMilkof = Calcification; 
        	}
             # print "%%%%%%%%%%%%%Calcification =  " Calcification   "   Ctype =   ", Ctype;
        }
}

if ($2 ~ /Type/) {
	split($3, array,"\"");
 #       print "Array 2 = " array[2];
        if (calc_scope == 1) {
			Ctype = array[2]; 
	}

        if ((array[2] == "Intramammary_Lymph_Node") ||  (array[2] == "Fibroadenoma") || (array[2] == Skin_Lesion) || (array[2] == "Lymph_Node")){  
		Lesion_type = array[2];
        }
        if (array[2] == "Trabecular_Thickening" ) {
		Trabecular_Thickening  = "Present";
        }
        if (array[2] == "Axillary_Adenopathy" ) {
		Axillary_Adenopathy  = "Present";
        }
        if (array[2] == "Architectual_Distortion" ) {
        	Architectual_Distortion = "Present";
        }
        if (array[2] == "Nipple_Retraction" ) {
		Nipple_Retraction  = "Present";
        }
	if (array[2]  == "Skin_Retraction") {
		Skin_Retraction  = "Present";
        }
	if (array[2]  == "Skin_Thickening") {
		Skin_Thickening  = "Present";
        }
}
}

/Size type/{ 
	split($3, array,"\""); 
#	print "Size    " array[2];
        if (array[2] <= 3) {
		size = "SMALL";
        }
        else if ((array[2] > 3) && (array[2] <= 7)) {
		size = "LARGE";
        }
	else if ((array[2] > 7) && (array[2] <= 8)) {
		size = "LARGE";
        }
	else { 
		size = "GIGANTIC"; 
        }
#        print array[2]"  "size;
}

/<\/Case>/ { 
# Reached end of record; print out CSV 
#print;
total_records++;
if (breastDensity != "*") {
breastDensity_cnt++;
}
if (masses_shape != "*") {
masses_shape_cnt++;
}
if (masses_margin != "*") {
masses_margin_cnt++;
}
if (masses_density != "*") {
masses_density_cnt++;
}
if (size != "*") {
size_cnt++;
}
if(Calcificationtype == "*"){
CalcificationType = extraneous_info;
extraneous_info = "*";

}
if ((lesion_type != "UNKNOWN") && (size != "GIGANTIC") && (Birads_score != 4)  && (Birads_score != 3) && (Birads_score != 0)) {
print diagnosis", "Birads_score", "breastDensity", "masses_shape", "masses_margin", "masses_density","Lesion_type", "hormone_treatment", "stability123", "tumorgrowth", "surgeryhx", "familyhx", "BreastHX", "age", "Trabecular_Thickening", " Axillary_Adenopathy", " Architectual_Distortion", " Nipple_Retraction", " Skin_Retraction", " Skin_Thickening", "calSuture", "calskin", "calPleomorph ", "calRod", "calCoarseHetero", "calMilkof" , "calDystro", "calRim", "calAmorphous", "calCoarse", "calEggshell", "calVasc", "calPunctate", "calLucent", "calLinear", "calGrouped", "calClustered", "calScattered", "calRegional", "calDiffuse", "calSingle", "  size;
}
calGrouped = "*";
calClustered = "*";
calScattered = "*";
calRegional = "*";
calDiffuse = "*";
calSingle = "*";
calSegmental = "*"; 
#print FILENAME
calSuture = "None";
#calDermal = "None";
calskin = "None";
calPleomorph = "None";
calRod = "None";
calCoarseHetero = "None";
calMilkof = "None";
calDystro = "None";
calRim = "None";
calAmorphous = "None";
calCoarse = "None";
calEggshell = "None";
calVasc = "None";
calPunctate = "None";
calLucent = "None";
calLinear = "None";
breastDensity = "*";
birads_category = "*";
masses_shape = "*";
masses_margin = "*";
masses_density = "*";
size = "*";
lesion_type = "*";
extraneous_info = "*";
Lesion_type = "*";
Lesion_properties = "*";
CalcificationType = "*";
Calcification = "*"; 
total_records = 0;
breastDensity = "*";
birads_category = "*";
masses_shape = "*";
masses_margin = "*";
masses_density = "*";
size = "*";
lesion_type = "*";

diagnosis = "*";
Birads_score = "*";
hormone_treatment = "*";
age = "*";
BreastHX = "*";
stability123 = "*";
tumorgrowth = "*";
surgeryhx = "*";
familyhx = "*";

Trabecular_Thickening  = "None";
Axillary_Adenopathy  = "None";
Architectual_Distortion = "None";
Nipple_Retraction  = "None";
Skin_Retraction  = "None";
Skin_Thickening  = "None";
};
END {
#print "records",  total_records, "breastDensity_cnt", breastDensity_cnt, "masses_shape_cnt", masses_shape_cnt, "masses_margin_cnt", masses_margin_cnt, "masses_density_cn
#t", masses_density_cnt, "size_cnt", size_cnt; 
}


