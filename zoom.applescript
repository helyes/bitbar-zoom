#!/usr/bin/osascript
# ./zoom.applescript --room=1234567890 --password=123456  --user="Andras"

to usage()
  log "\nUsage: zoom.applescript --room=1234567890 --user=John Doe [--password=123456]\n"
end usage

on run argv
  set zoom to "zoom.us"
  set params to getParams(argv)

  -- password is optional
  try
    set pwd to pwd of params
  on error
    set pwd to "-"
  end try

  if pwd is not "-"
    log "\nJoining to room " & room of params & " as " & uname of params & "/" & pwd
  else
    log "\nJoining to room " & room of params & " as " & uname of params
  end if
  
  if application zoom is not running then
    log "Starting up " & zoom & "..."
    tell application zoom to activate
    delay 4.0
  end if
	
	tell application "System Events"
   
		tell process zoom
      delay 1.0
      click menu item "Join Meeting..." of menu "Zoom.us" of menu bar 1
      delay 2.0
      
      set joinMeetingWindow to window 1

      set idField to text field 1 of joinMeetingWindow
      set nameField to text field 2 of joinMeetingWindow
      set joinButton to button 2 of joinMeetingWindow
      
			--UI elements of joinMeetingWindow
      --UI elements of window 1
      set value of idField to room of params
      set value of nameField to uname of params
      delay 1.0
      click joinButton

      if pwd is not "-"
        try
          delay 3.0
          set passwordField to text field "Meeting Password edit" of joinMeetingWindow
          set joinButton to button 1 of joinMeetingWindow

          set value of passwordField to pwd
          
          delay 0.5
          click joinButton
        end try
      end if

		end tell -- process zoom
	end tell -- system events

end run

-- transforms key=value into [key, value] array
on splitString(theString, theDelimiter)
  set oldDelimiters to AppleScript's text item delimiters
  set AppleScript's text item delimiters to theDelimiter
  set theArray to every text item of theString
  set AppleScript's text item delimiters to oldDelimiters
  return theArray
end splitString

to getParams(parameters)
  set params to { }
  try
    -- there should be at least two params
    if (count of parameters) < 2
      usage()
      error "missing params"
    end if

    repeat with arg in parameters
      set parts to splitString(arg, "=")
      
      -- accept only key=value
      if (count of parts) is not 2
        usage()
        error "paremeter error, parameter value is null, use key=value format. Param: " & parts number 1
      end if

      set paramkey to item 1 of parts
      set paramValue to item 2 of parts
      if paramkey is "--user"
        set params to params & {uname:paramValue}
      else if paramkey is "--room"
        set params to params & {room:paramValue}
      else if paramkey is "--password"
        set params to params & {pwd:paramValue}
      else
        usage()
        error "unknown parameter: " & item 1 of parts number 1
      end if

    end repeat

  on error error_message number error_number
    set this_error to "[" & error_number & "]\n\n" & "Error: " & error_message
    --log "\nError: " & this_error
    tell me to error this_error number 1  
  end try

end getparams
