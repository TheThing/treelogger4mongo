treelogger4mongo
================

The treelogger4mongo is a simple module that allows you to lo debug data into a mongo database. The only difference is that this module supports logging in a tree-like structure.

## How does it work?

Lets imagine we have a process that has to loop through all your user database. Adding the mongo logger would only have to be something like this:

    import treelogger4mongo as treelog

    def process_users(users):
    	branch = treelog.info("About to process %s users." % len(users))
        for user in users:
            sub = branch.info("Processing: %s" % user.username,
                        {'username': user.username,
                         'email': user.email})
            #do something with user.
            sub.info("Did something with user.")
            #something else
            if user.is_special:
            	some_heavy_function(user, sub.info("Starting some_heavy_function."))
            sub.info("Finished processing.")

What we get from this is a root log entry with the message "About to process ... users.". However, this is where treelogger comes strong in, each log message after that is applied like a branch to that root log entry.

A sample output would be a log structure in mongo that looks something like this:

    About to process 2 users
    ├───Processing John Doe {username: johndoe, email: }
    │   ├───Did something with user.
    │   └───Finished processing
    └───Processing John Smith
        ├───Did something with user.
        ├───Starting some_heavy_function.
        │   └───....
        └───Finished processing

With this, you get a nice tree structure for your logs in mongo that makes it easier to read the log and trace each function.

**Hint:**

Each branch can, including a simple message, contain any arbitrary information in the data parameter. This accepts any object and is automatically saved with the log entry.

## Getting it to run

In order to be able to dynamically call treelogger4mongo, you need to have initialized it atlease once somewhere. The treelogger4mongo automatically saves the configuration and allows you to call its static functions.

    from treelogger4mongo import Tree

    Tree("host", "port", "database", "collection")