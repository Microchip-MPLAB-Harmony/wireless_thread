    
    /*Open Thread System Initialization*/
    otSysInit(0U,0U);
    
    /* Creation of openthread Task Queue */
    OSAL_QUEUE_Create(&OTQueue, OT_TASK_QUEUE_SIZE, sizeof(OT_Msg_T));
