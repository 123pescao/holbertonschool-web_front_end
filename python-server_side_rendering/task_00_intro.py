#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitations from a template and a list of attendees.
    """
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees):
        personalized_invite = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        file_name = f'output_{i + 1}.txt'
        with open(file_name, 'w') as file:
            file.write(personalized_invite)
        print(f"Generated: {file_name}")
