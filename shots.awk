#!/bin/awk -f

/^weapon_fire$/ { 
		getline;
		getline;
		getline;
		x=substr($2, 0, length($2)-1);
		y=substr($3, 0, length($3)-1);
		z=$4;
		getline;
		getline;
		team = $2;
		getline;
		weapon=$2;
		print x,y,z,team, weapon}
