Git Conflict and How to Resolve It

A git conflict happens when two people working on the same project edit the same part of a file and try to push or merge their changes. Git cannot automatically combine the changes because they are different, so it stops the process and shows an error message indicating a conflict.

During our class simulation, we worked in pairs. One person pushed changes, and another person also made changes to the same file. When the second person tried to push or pull the updates, Git showed a conflict.

Steps to Resolve a Git Conflict
	1.	Try to push or pull changes.
	2.	Git shows an error message saying there is a merge conflict.
	3.	Open the conflicted file in VS Code (it is usually marked in the Source Control panel).
	4.	Click on the file, and VS Code automatically shows a split view.
	5.	The split view shows:
	•	Current Change (the version already in the branch)
	•	Incoming Change (the version being merged)
	6.	Choose one of the options:
	•	Accept Current Change
	•	Accept Incoming Change
	•	Accept Both Changes
	7.	Save the file after selecting the correct version.
	8.	Stage the file using git add.
	9.	Complete the merge using git commit.
	10.	Push the changes again.

After completing these steps, the conflict is resolved and the project can continue normally.

