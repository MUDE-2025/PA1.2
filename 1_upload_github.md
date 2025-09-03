# Upload files to GitHub and check for pass

You'll be assigned repositories on GitHub for the assignments to be delivered. We will learn more about Git, GitHub and repositories next week. For now, we will simply be using it as a place to download and upload files, and to check whether you succeeded the PA. Only you (and your fellow group members for group assignments) and your teachers have access to this repository.

To work on the assignment, you are expected to first download the files from the repository, then work in the notebook. When you have finished the activities, you'll upload your files back to the GitHub repository online. We'll learn a smarter way to do this next week, but this will work for now.

## Task 1.1 Access the assignment

1. Click the link here, the same one as provided in the [README.md](./README.md): [classroom.github.com/a/...](TBP)
2. Authorize GitHub Access
3. Join the classroom and identify yourself by finding your Student ID Number in the list of "Identifiers". If your ID is not there, please inform MUDE-CEG@tudelft.nl but you can "skip this step" (username will be used for repo name)
4. Click "Accept this assignment"
5. you will see a link that looks like this: `http://github.com/MUDE-2025/....` 

![Successfully created assignment](https://files.mude.citg.tudelft.nl/created_github_assignment.png)

6. Click the link, it'll bring you to your personal repository. Save the link or bookmark it so you can find it later

![An example of the repository for your assignment](https://files.mude.citg.tudelft.nl/example_repo_github.png)

## Task 1.2 Download the assignment

1. Click the green "Code" button
2. At the bottom of the popup window, select "Download ZIP"
3. Unzip the file on your computer; the unzipped folder will be your working directory for PA 1.3 and contains all necessary files. Remember that the concept of _working directory_ was introduced in the [reading of last week](https://mude.citg.tudelft.nl/book/2025/programming/week_1_1/files.html); it would be a good idea to make sure the files from this PA are all stored within your MUDE directory so they are easy to find if you need them later!

![How to download the assignment](https://files.mude.citg.tudelft.nl/how_to_download_assignment.png)

## Task 1.3 Upload files

To practice on how to submit your assignment, you'll upload a dummy file.

1. Download the [zip of the dummy file](https://files.mude.citg.tudelft.nl/file_to_upload.zip)
2. Unzip the dummy file.
3. Click the "Add file" button and then select "Upload Files"
4. Drag the file you changed (for now the file to be uploaded) to the appropriate box, or find it using the "Browse" feature.
5. Once the file is there you don't have to edit any text (e.g., the commit messages)
6. Simply click the green "Commit Changes" button.
7. That's it!

![How to upload a file](https://files.mude.citg.tudelft.nl/how_to_upload_file.png)

## Task 1.4 Check that you passed the PA

To see if you passed the PA

1. Start in the home page of your PA 1.3 repository (should be taken there automatically after you submit the file).
2. Click on the "Actions" tab near the top center of the page.
3. If you recently uploaded a file you should see a yellow dot. This means your submission is being checked; it will change after the checking process is completed.
4. If the dot turns green, you passed the PA. Probably it doesn't turn green because you didn't start the second part of this assignment.

![Passed PA](https://files.mude.citg.tudelft.nl/passed_notebook.png)

If the dot turns red with an "x" it means your PA does not meet the requirements. If this happens, you can find more details by clicking on the workflow:

![Failed PA](https://files.mude.citg.tudelft.nl/failed_notebook.png)

Clicking on `run-autograding-tests` gives you an overview of which parts you failed and if you open the individual checks some more details. E.g. in the figure below, 0 points are scored because 'Check for file_to_upload.md' gives `file_to_upload.md not found`.

![Failed PA details](https://files.mude.citg.tudelft.nl/failed_notebook_2.png)


> By Tom van Woudenberg, Robert Lanzafame and Jialei Ding, Delft University of Technology. CC BY 4.0, more info [on the Credits page of Workbook](https://mude.citg.tudelft.nl/workbook-2025/credits.html).