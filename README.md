# tfm_unir_back

/login
    POST
        USERNAME
        PASSWORD
/logout
    POST
        TOKEN
/user
    POST
        USERNAME
        FULLNAME
        PASSWORD
    GET
        TOKEN
/transaction
    POST
        TOKEN
        AMOUNT
        DESCRIPTION
    GET
        TOKEN
        ?FROMDATE
/balance
    GET
        TOKEN