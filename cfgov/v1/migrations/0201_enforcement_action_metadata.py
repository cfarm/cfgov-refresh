# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-31 18:25
from __future__ import unicode_literals

from django.db import migrations
import v1.atomic_elements.molecules
import v1.blocks
import v1.models.snippets
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailsnippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0200_expandable_group_help_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfgovpage',
            name='sidefoot',
            field=wagtail.wagtailcore.fields.StreamField((('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('button', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')])))))))), ('related_links', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False))))))))), ('related_posts', wagtail.wagtailcore.blocks.StructBlock((('limit', wagtail.wagtailcore.blocks.CharBlock(default='3', help_text='This limit applies to EACH TYPE of post this module retrieves, not the total number of retrieved posts.')), ('show_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='This toggles the heading and icon for the related types.', label='Show Heading and Icon?', required=False)), ('header_title', wagtail.wagtailcore.blocks.CharBlock(default='Further reading', label='Slug Title')), ('relate_posts', wagtail.wagtailcore.blocks.BooleanBlock(default=True, editable=False, label='Blog Posts', required=False)), ('relate_newsroom', wagtail.wagtailcore.blocks.BooleanBlock(default=True, editable=False, label='Newsroom', required=False)), ('relate_events', wagtail.wagtailcore.blocks.BooleanBlock(default=True, label='Events', required=False)), ('specific_categories', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('Blog', (('At the CFPB', 'At the CFPB'), ('Policy &amp; Compliance', 'Policy and compliance'), ('Data, Research &amp; Reports', 'Data, research, and reports'), ('Info for Consumers', 'Info for consumers'))), ('Newsroom', (('Op-Ed', 'Op-ed'), ('Press Release', 'Press release'), ('Speech', 'Speech'), ('Testimony', 'Testimony'), ("Director's notebook", "Director's notebook")))], required=False), required=False)), ('and_filtering', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='If checked, related posts will only be pulled in if they match ALL topic tags set on this page. Otherwise, related posts can match any one topic tag.', label='Match all topic tags', required=False)), ('alternate_view_more_url', wagtail.wagtailcore.blocks.CharBlock(help_text='By default, the "View more" link will go to the Activity Log, filtered based on the above parameters. Enter a URL in this field to override that link destination.', label='Alternate "View more" URL', required=False))))), ('related_metadata', wagtail.wagtailcore.blocks.StructBlock((('slug', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), ('content', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), ('blob', wagtail.wagtailcore.blocks.RichTextBlock())), icon='pilcrow')), ('list', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False))))))), icon='list-ul')), ('date', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), ('date', wagtail.wagtailcore.blocks.DateBlock())), icon='date')), ('topics', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(default='Topics', max_length=100)), ('show_topics', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False))), icon='tag')), ('categories', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(default='Categories', max_length=100)), ('show_categories', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False))), icon='list-ul'))))), ('is_half_width', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))))), ('enforcement_action_metadata', wagtail.wagtailcore.blocks.StructBlock((('slug', wagtail.wagtailcore.blocks.CharBlock(default='Action details', max_length=100)), ('categories', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), ('court', wagtail.wagtailcore.blocks.CharBlock(max_length=150, required=True)), ('institution_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('Nonbank', 'Nonbank'), ('Bank', 'Bank')])), ('status', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('Post Order/Post Judgment', 'Post Order/Post Judgment'), ('Expired/Terminated/Dismissed', 'Expired/Terminated/Dismissed'), ('Pending Litigation', 'Pending Litigation')])), ('docket_number', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=True)), ('topics', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), ('date_filed', wagtail.wagtailcore.blocks.DateBlock())))), ('email_signup', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))))), ('sidebar_contact', wagtail.wagtailcore.blocks.StructBlock((('contact', wagtail.wagtailsnippets.blocks.SnippetChooserBlock('v1.Contact')), ('has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Add a horizontal rule line to top of contact block.', required=False))))), ('rss_feed', v1.atomic_elements.molecules.RSSFeed()), ('social_media', wagtail.wagtailcore.blocks.StructBlock((('is_share_view', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='If unchecked, social media icons will link users to official CFPB accounts. Do not fill in any further fields.', label='Desired action: share this page', required=False)), ('blurb', wagtail.wagtailcore.blocks.CharBlock(default="Look what I found on the CFPB's site!", help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False)), ('twitter_text', wagtail.wagtailcore.blocks.CharBlock(help_text='(Optional) Custom text for Twitter shares. If blank, will default to value of blurb field above.', max_length=100, required=False)), ('twitter_related', wagtail.wagtailcore.blocks.CharBlock(help_text='(Optional) A comma-separated list of accounts related to the content of the shared URL. Do not enter the  @ symbol. If blank, it will default to just "cfpb".', required=False)), ('twitter_hashtags', wagtail.wagtailcore.blocks.CharBlock(help_text='(Optional) A comma-separated list of hashtags to be appended to default tweet text.', required=False)), ('twitter_lang', wagtail.wagtailcore.blocks.CharBlock(help_text='(Optional) Loads text components in the specified language, if other than English. E.g., use "es"  for Spanish. See https://dev.twitter.com/web/overview/languages for a list of supported language codes.', required=False)), ('email_title', wagtail.wagtailcore.blocks.CharBlock(help_text='(Optional) Custom subject for email shares. If blank, will default to value of blurb field above.', required=False)), ('email_text', wagtail.wagtailcore.blocks.CharBlock(help_text='(Optional) Custom text for email shares. If blank, will default to "Check out this page from the CFPB".', required=False)), ('email_signature', wagtail.wagtailcore.blocks.CharBlock(help_text='(Optional) Adds a custom signature line to email shares. ', required=False)), ('linkedin_title', wagtail.wagtailcore.blocks.CharBlock(help_text='(Optional) Custom title for LinkedIn shares. If blank, will default to value of blurb field above.', required=False)), ('linkedin_text', wagtail.wagtailcore.blocks.CharBlock(help_text='(Optional) Custom text for LinkedIn shares.', required=False))))), ('reusable_text', v1.blocks.ReusableTextChooserBlock(v1.models.snippets.ReusableText))), blank=True),
        ),
    ]
