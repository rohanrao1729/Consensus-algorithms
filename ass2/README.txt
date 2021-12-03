/****************************** Consensus Implementation  *******************/


/****GROUP DETAILS*******/
Group NO:27

Group Members:
--------------------
1.NALLANI ROHAN RAO(2019A7PS0048H)
2.Durgavarapu Sri Krishna Karthik(2019A7PS0189H)
3.Doni Akhil Lohith(2019A7PS0026H)

-------------------------------------------------------------------------------------------------

Where did we add new lines of code:
-----------------------------------------
In the Start.java file whereever there is////****************NEWLY ADDED********** all those lines and classes preceeding are newly added for PoS implementation.

New Classes Added:
------------------------------------
1.Node 
2.ValidatorNode
3.Blockchain
4.Consensus
->Few more methods and lines of code added


How do we decide the next Validator?
-----------------------------------
We take any random criteria ie from 
1.coinage of a validator 
2.Deposit of a validator
3.CompPower of  a validator 
4.probabilistic combination of the above three

For example the one with the highest stake is selected and given less priority for future validations and with time the priority also again increases ensuring equal chances of validation of block restricting monopoly.

Also in times of confusion for validator follows the longest chain rule

Nodes:
-----------
1.Normal Nodes
2.Validator Nodes is special node which is capable of adding a block to blockchain by putting something at stake
ValidatorNode class extends Node class in the code.

To run:
-----------------------
1.Give input transactions in fxt.txt 
(or) run the script transactionsGen.py to get random set of transactions

2.javac Start.java
3.java Start

To execute transactionGen.py
--------------------------
python transactionGen.py

output goes to fotxt.txt 

