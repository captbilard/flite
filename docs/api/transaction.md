# Transactions
Supports deposits, withdrawals,Peer-to-Peer Transfer, viewing transactions.

## Initiates a Deposits

**Deposits**:

`POST` `/users/:userid/deposits/`

Parameters:

*Note:*

- Authorization Protected
- Assumes account is credited when a POST is made

**Response**:

```json
Content-Type application/json
200 OK

{
    "message": "Your account has been credited"
}
```


## Initiates a Withdrawal

**Withdrawal**:

`POST` `/users/:userid/withdrawal/`

Parameters:

*Note:*

- Authorization Protected
- Assumes account is debited when a POST is made

**Response**:

```json
Content-Type application/json
200 OK


{
    "message": "Withdrawal successful & account balance updated"
}
```



## Peer-to-Peer Transfer

**Request**:

`POST` `/account/:sender_account_id/transfers/:recipient_account_id`

Parameters:
Name       | Type   | Description
-----------|--------|---
sender     | uuid   | The id of the sender.
receipient | uuid   | The id of the receipient.


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "message": "Transfer successful",
    "from": "sender",
    "to": "receipient",
    "Ref. Number": "490311714200",
    "status": "Successful",
    "new_balance": 0.0
}
```


## List of Transactions from a user

**Request**:

`GET` `/account/:account_id/transactions/`

Parameters:




*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "a77518fd-14ad-4427-a840-7f25ba2f12e7",
            "created": "2021-06-11T15:28:43+0100",
            "modified": "2021-06-11T15:28:44+0100",
            "reference": "931265282373",
            "status": "Failed",
            "amount": 0.0,
            "new_balance": 0.0,
            "owner": "288e35fa-d370-4ae6-8a99-6ee575016343"
        }
    ]
}

```


## Get a particular user transaction details

**Request**:

`GET` `/account/:account_id/transactions/:transaction_id`

Parameters:


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "id": "a77518fd-14ad-4427-a840-7f25ba2f12e7",
    "created": "2021-06-11T15:28:43+0100",
    "modified": "2021-06-11T15:28:44+0100",
    "reference": "931265282373",
    "status": "Failed",
    "amount": 0.0,
    "new_balance": 0.0,
    "owner": "288e35fa-d370-4ae6-8a99-6ee575016343"
}
```