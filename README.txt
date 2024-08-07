This is our simple Database project for our college Assignment.

The database name is expense_tracker 


Tables inside expense_tracker

wallet{
	
	W_no int primary_key
	Name varchar
	Give_and_Take int

}

credit{

	C_No int auto_increment primary
	c_From varchar
	Description varchar(50)
	Credit_amount int
	W_No int Mul
	c_timestamp timestamp on update CURRENT_TIMESTAMP

}


debit{

	D_No int auto_increment primary 
	category varchar
	item varchar
	amount int
	ret varchar
	W_No int
	timestamp timestamp on update CURRENT_TIMESTAMP

}

target{

	targeton varchar(30)
	amount int
}