(void) xTaskCreate(taskOpenThread,
                       "ot-task",
                       1024,
                       NULL,
                       3,
                       &taskHandleOpenThread);
