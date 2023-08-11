(void) xTaskCreate(taskOpenThread,
                       "ot-task",
                       4096,
                       NULL,
                       3,
                       &taskHandleOpenThread);
