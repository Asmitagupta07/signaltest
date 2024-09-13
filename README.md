Django Signals
Question 1: Synchronous or Asynchronous?
By default, Django signals are executed synchronously. This means that the signal handler function is called immediately after the signal is sent, within the same execution context.
Code Snippet:

![image](https://github.com/user-attachments/assets/7aeec403-453b-40e1-8061-904fa89d52f1)

In this example, the my_handler function will be executed immediately after the MyModel object is saved.

Question 2: Same Thread?
Yes, Django signals by default run in the same thread as the caller. This means that the signal handler function will be executed in the same thread that triggered the signal.
Code Snippet:
![image](https://github.com/user-attachments/assets/f0498240-0244-4880-9316-a01f28a1369d)

In this example, the my_handler function (if defined) will be executed in the same thread as the my_function function.

Question 3: Same Database Transaction?
By default, Django signals do not run in the same database transaction as the caller. This means that any changes made in the signal handler function will be committed in a separate transaction.
Code Snippet:

![image](https://github.com/user-attachments/assets/2cf7cb61-952f-412c-9c19-5c871ee57232)


In this example, the changes made to OtherModel will be committed in a separate transaction from the original save of the MyModel object.

Custom Classes in Python

Rectangle Class
![image](https://github.com/user-attachments/assets/64eec80d-d7cb-41a3-a260-c2c2d01986d4)

Output
![image](https://github.com/user-attachments/assets/21d460de-81a5-4482-a16b-b59ebe71d366)

This Rectangle class satisfies the given requirements:

It requires length and width to be initialized.
It can be iterated over.
When iterated, it yields two dictionaries containing the length and width values.
