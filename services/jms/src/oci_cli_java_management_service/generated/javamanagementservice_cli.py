# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('jms.jms_root_group.command_name', 'jms'), cls=CommandGroupWithAlias, help=cli_util.override('jms.jms_root_group.help', """API for the Java Management Service. Use this API to view and manage Fleets."""), short_help=cli_util.override('jms.jms_root_group.short_help', """Java Management Service Query API"""))
@cli_util.help_option_group
def jms_root_group():
    pass


@click.command(cli_util.override('jms.managed_instance_usage_group.command_name', 'managed-instance-usage'), cls=CommandGroupWithAlias, help="""Managed instance usage during a specified time period. An entity that emits usage events to Java Management Service (JMS) is represented as a managed instance. A managed instance has a unique identity which is used by JMS to distinguish it from other managed instances. Currently, JMS supports only one kind of managed instance, a Management Agent.""")
@cli_util.help_option_group
def managed_instance_usage_group():
    pass


@click.command(cli_util.override('jms.fleet_group.command_name', 'fleet'), cls=CommandGroupWithAlias, help="""A Fleet is the primary collection with which users interact when using Java Management Service.""")
@cli_util.help_option_group
def fleet_group():
    pass


@click.command(cli_util.override('jms.fleet_agent_configuration_group.command_name', 'fleet-agent-configuration'), cls=CommandGroupWithAlias, help="""Management Agent Configuration for a Fleet. Includes JRE scanning frequency and list of include/exclude file system paths.""")
@cli_util.help_option_group
def fleet_agent_configuration_group():
    pass


@click.command(cli_util.override('jms.application_usage_group.command_name', 'application-usage'), cls=CommandGroupWithAlias, help="""Application usage during a specified time period. An application is a Java application that can be executed by a Java Runtime installation. An application is independent of the Java Runtime or its installation.""")
@cli_util.help_option_group
def application_usage_group():
    pass


@click.command(cli_util.override('jms.installation_usage_group.command_name', 'installation-usage'), cls=CommandGroupWithAlias, help="""Installation usage during a specified time period. An installation is a collection of deployed instances of a specific Java Runtime that share the same install path.""")
@cli_util.help_option_group
def installation_usage_group():
    pass


@click.command(cli_util.override('jms.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('jms.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('jms.jre_usage_group.command_name', 'jre-usage'), cls=CommandGroupWithAlias, help="""Java Runtime usage during a specified time period. A Java Runtime is identified by its vendor and version.""")
@cli_util.help_option_group
def jre_usage_group():
    pass


@click.command(cli_util.override('jms.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request. See [Work Requests].""")
@cli_util.help_option_group
def work_request_group():
    pass


jms_root_group.add_command(managed_instance_usage_group)
jms_root_group.add_command(fleet_group)
jms_root_group.add_command(fleet_agent_configuration_group)
jms_root_group.add_command(application_usage_group)
jms_root_group.add_command(installation_usage_group)
jms_root_group.add_command(work_request_error_group)
jms_root_group.add_command(work_request_log_entry_group)
jms_root_group.add_command(jre_usage_group)
jms_root_group.add_command(work_request_group)


@fleet_group.command(name=cli_util.override('jms.change_fleet_compartment.command_name', 'change-compartment'), help=u"""Move a specified Fleet into the compartment identified in the POST form. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeFleetCompartment)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the Fleet should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_fleet_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fleet_id, compartment_id, if_match):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.change_fleet_compartment(
        fleet_id=fleet_id,
        change_fleet_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fleet_group.command(name=cli_util.override('jms.create_fleet.command_name', 'create'), help=u"""Create a new Fleet using the information provided. \n[Command Reference](createFleet)""")
@cli_util.option('--display-name', required=True, help=u"""The name of the Fleet. The displayName must be unique for Fleets in the same compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment of the Fleet.""")
@cli_util.option('--description', help=u"""The Fleet's description. If nothing is provided, the Fleet description will be null.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See [Understanding Free-form Tags]).""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See [Managing Tags and Tag Namespaces].)""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'jms', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'jms', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'jms', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'jms', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def create_fleet(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, description, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.create_fleet(
        create_fleet_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fleet_group.command(name=cli_util.override('jms.delete_fleet.command_name', 'delete'), help=u"""Deletes the Fleet specified by an identifier. \n[Command Reference](deleteFleet)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_fleet(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fleet_id, if_match):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.delete_fleet(
        fleet_id=fleet_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fleet_group.command(name=cli_util.override('jms.get_fleet.command_name', 'get'), help=u"""Retrieve a Fleet with the specified identifier. \n[Command Reference](getFleet)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'Fleet'})
@cli_util.wrap_exceptions
def get_fleet(ctx, from_json, fleet_id):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.get_fleet(
        fleet_id=fleet_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fleet_agent_configuration_group.command(name=cli_util.override('jms.get_fleet_agent_configuration.command_name', 'get'), help=u"""Retrieve a Fleet Agent Configuration for the specified Fleet. \n[Command Reference](getFleetAgentConfiguration)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'FleetAgentConfiguration'})
@cli_util.wrap_exceptions
def get_fleet_agent_configuration(ctx, from_json, fleet_id):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.get_fleet_agent_configuration(
        fleet_id=fleet_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('jms.get_work_request.command_name', 'get'), help=u"""Retrieve the details of a work request with the specified ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the asynchronous work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fleet_group.command(name=cli_util.override('jms.list_fleets.command_name', 'list'), help=u"""Returns a list of all the Fleets contained by a compartment. \n[Command Reference](listFleets)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""The ID of the Fleet.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), help=u"""The state of the lifecycle.""")
@cli_util.option('--display-name', help=u"""The display name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "timeCreated"]), help=u"""The field to sort Fleets. Only one sort order may be provided. Default order for _timeCreated_, _approximateJreCount_, _approximateInstallationCount_, _approximateApplicationCount_ and _approximateManagedInstanceCount_  is **descending**. Default order for _displayName_ is **ascending**. If no value is specified _timeCreated_ is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'FleetCollection'})
@cli_util.wrap_exceptions
def list_fleets(ctx, from_json, all_pages, page_size, compartment_id, id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_fleets,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_fleets,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_fleets(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('jms.list_work_request_errors.command_name', 'list'), help=u"""Retrieve a (paginated) list of errors for a specified work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('jms.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Retrieve a (paginated) list of logs for a specified work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('jms.list_work_requests.command_name', 'list'), help=u"""List the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""The ID of an asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if id is not None:
        kwargs['id'] = id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@application_usage_group.command(name=cli_util.override('jms.request_summarized_application_usage.command_name', 'request-summarized'), help=u"""List application usage in a specified Fleet filtered by form parameters. \n[Command Reference](requestSummarizedApplicationUsage)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""The start of the time period during which resources are searched (formatted according to RFC3339). Defaults to current time minus seven days.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""The end of the time period during which resources are searched (formatted according to RFC3339). Defaults to current time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--display-name', help=u"""The display name of the application.""")
@cli_util.option('--installation-path', help=u"""The installation path of the related installation.""")
@cli_util.option('--jre-vendor', help=u"""The vendor of the related Java Runtime.""")
@cli_util.option('--jre-distribution', help=u"""The distribution of the related Java Runtime.""")
@cli_util.option('--jre-version', help=u"""The version of the related Java Runtime.""")
@cli_util.option('--application-id', help=u"""The ID of the application.""")
@cli_util.option('--application-type', help=u"""The way the application was started.""")
@cli_util.option('--managed-instance-id', help=u"""The ID of the related managed instance.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeFirstSeen", "timeLastSeen", "displayName", "approximateJreCount", "approximateInstallationCount", "approximateManagedInstanceCount"]), help=u"""The field to sort application views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, _approximateJreCount_, _approximateInstallationCount_ and _approximateManagedInstanceCount_  is **descending**. Default order for _displayName_ is **ascending**. If no value is specified _timeLastSeen_ is default.""")
@cli_util.option('--fields', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateJreCount', 'approximateInstallationCount' and 'approximateManagedInstanceCount'. For example 'approximateJreCount,approximateInstallationCount'.

This option is a JSON list with items of type SummarizeApplicationUsageFields.  For documentation on SummarizeApplicationUsageFields please see our API reference: https://docs.cloud.oracle.com/api/#/en/javamanagementservice/20210610/datatypes/SummarizeApplicationUsageFields.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'jms', 'class': 'list[SummarizeApplicationUsageFields]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'jms', 'class': 'list[SummarizeApplicationUsageFields]'}}, output_type={'module': 'jms', 'class': 'ApplicationUsageCollection'})
@cli_util.wrap_exceptions
def request_summarized_application_usage(ctx, from_json, fleet_id, time_start, time_end, display_name, installation_path, jre_vendor, jre_distribution, jre_version, application_id, application_type, managed_instance_id, sort_order, sort_by, fields, limit, page):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_start is not None:
        _details['timeStart'] = time_start

    if time_end is not None:
        _details['timeEnd'] = time_end

    if display_name is not None:
        _details['displayName'] = display_name

    if installation_path is not None:
        _details['installationPath'] = installation_path

    if jre_vendor is not None:
        _details['jreVendor'] = jre_vendor

    if jre_distribution is not None:
        _details['jreDistribution'] = jre_distribution

    if jre_version is not None:
        _details['jreVersion'] = jre_version

    if application_id is not None:
        _details['applicationId'] = application_id

    if application_type is not None:
        _details['applicationType'] = application_type

    if managed_instance_id is not None:
        _details['managedInstanceId'] = managed_instance_id

    if sort_order is not None:
        _details['sortOrder'] = sort_order

    if sort_by is not None:
        _details['sortBy'] = sort_by

    if fields is not None:
        _details['fields'] = cli_util.parse_json_parameter("fields", fields)

    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.request_summarized_application_usage(
        fleet_id=fleet_id,
        request_summarized_application_usage_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@installation_usage_group.command(name=cli_util.override('jms.request_summarized_installation_usage.command_name', 'request-summarized'), help=u"""List Java installation usage in a specified Fleet filtered by form parameters. \n[Command Reference](requestSummarizedInstallationUsage)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""The start of the time period during which resources are searched (formatted according to RFC3339). Defaults to current time minus seven days.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""The end of the time period during which resources are searched (formatted according to RFC3339). Defaults to current time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--installation-path', help=u"""The path of the installation.""")
@cli_util.option('--jre-vendor', help=u"""The vendor of the related Java Runtime.""")
@cli_util.option('--jre-distribution', help=u"""The distribution of the related Java Runtime.""")
@cli_util.option('--jre-version', help=u"""The version of the related Java Runtime.""")
@cli_util.option('--application-id', help=u"""The ID of the related application.""")
@cli_util.option('--managed-instance-id', help=u"""The ID of the related managed instance.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["jreDistribution", "jreVendor", "jreVersion", "path", "timeFirstSeen", "timeLastSeen", "approximateApplicationCount", "approximateManagedInstanceCount"]), help=u"""The field to sort installation views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, _jreVersion_, _approximateApplicationCount_ and _approximateManagedInstanceCount_  is **descending**. Default order for _jreDistribution_ and _jreVendor_ is **ascending**. If no value is specified _timeLastSeen_ is default.""")
@cli_util.option('--fields', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateApplicationCount' and 'approximateManagedInstanceCount'. For example 'approximateApplicationCount,approximateManagedInstanceCount'.

This option is a JSON list with items of type SummarizeInstallationUsageFields.  For documentation on SummarizeInstallationUsageFields please see our API reference: https://docs.cloud.oracle.com/api/#/en/javamanagementservice/20210610/datatypes/SummarizeInstallationUsageFields.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'jms', 'class': 'list[SummarizeInstallationUsageFields]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'jms', 'class': 'list[SummarizeInstallationUsageFields]'}}, output_type={'module': 'jms', 'class': 'InstallationUsageCollection'})
@cli_util.wrap_exceptions
def request_summarized_installation_usage(ctx, from_json, fleet_id, time_start, time_end, installation_path, jre_vendor, jre_distribution, jre_version, application_id, managed_instance_id, sort_order, sort_by, fields, limit, page):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_start is not None:
        _details['timeStart'] = time_start

    if time_end is not None:
        _details['timeEnd'] = time_end

    if installation_path is not None:
        _details['installationPath'] = installation_path

    if jre_vendor is not None:
        _details['jreVendor'] = jre_vendor

    if jre_distribution is not None:
        _details['jreDistribution'] = jre_distribution

    if jre_version is not None:
        _details['jreVersion'] = jre_version

    if application_id is not None:
        _details['applicationId'] = application_id

    if managed_instance_id is not None:
        _details['managedInstanceId'] = managed_instance_id

    if sort_order is not None:
        _details['sortOrder'] = sort_order

    if sort_by is not None:
        _details['sortBy'] = sort_by

    if fields is not None:
        _details['fields'] = cli_util.parse_json_parameter("fields", fields)

    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.request_summarized_installation_usage(
        fleet_id=fleet_id,
        request_summarized_installation_usage_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@jre_usage_group.command(name=cli_util.override('jms.request_summarized_jre_usage.command_name', 'request-summarized'), help=u"""List Java Runtime usage in a specified Fleet filtered by form parameters. \n[Command Reference](requestSummarizedJreUsage)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""The start of the time period during which resources are searched (formatted according to RFC3339). Defaults to current time minus seven days.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""The end of the time period during which resources are searched (formatted according to RFC3339). Defaults to current time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--jre-vendor', help=u"""The vendor of the Java Runtime.""")
@cli_util.option('--jre-distribution', help=u"""The distribution of the Java Runtime.""")
@cli_util.option('--jre-version', help=u"""The version of the Java Runtime.""")
@cli_util.option('--application-id', help=u"""The ID of the related application.""")
@cli_util.option('--managed-instance-id', help=u"""The [OCID] of the related managed instance.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["distribution", "timeFirstSeen", "timeLastSeen", "vendor", "version", "approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount"]), help=u"""The field to sort Java Runtime views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, _version_, _approximateInstallationCount_, _approximateApplicationCount_ and _approximateManagedInstanceCount_  is **descending**. Default order for _distribution_ and _vendor_ is **ascending**. If no value is specified _timeLastSeen_ is default.""")
@cli_util.option('--fields', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateApplicationCount', 'approximateInstallationCount' and 'approximateManagedInstanceCount'. For example 'approximateApplicationCount,approximateManagedInstanceCount'.

This option is a JSON list with items of type SummarizeJreUsageFields.  For documentation on SummarizeJreUsageFields please see our API reference: https://docs.cloud.oracle.com/api/#/en/javamanagementservice/20210610/datatypes/SummarizeJreUsageFields.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'jms', 'class': 'list[SummarizeJreUsageFields]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'jms', 'class': 'list[SummarizeJreUsageFields]'}}, output_type={'module': 'jms', 'class': 'JreUsageCollection'})
@cli_util.wrap_exceptions
def request_summarized_jre_usage(ctx, from_json, fleet_id, time_start, time_end, jre_vendor, jre_distribution, jre_version, application_id, managed_instance_id, sort_order, sort_by, fields, limit, page):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_start is not None:
        _details['timeStart'] = time_start

    if time_end is not None:
        _details['timeEnd'] = time_end

    if jre_vendor is not None:
        _details['jreVendor'] = jre_vendor

    if jre_distribution is not None:
        _details['jreDistribution'] = jre_distribution

    if jre_version is not None:
        _details['jreVersion'] = jre_version

    if application_id is not None:
        _details['applicationId'] = application_id

    if managed_instance_id is not None:
        _details['managedInstanceId'] = managed_instance_id

    if sort_order is not None:
        _details['sortOrder'] = sort_order

    if sort_by is not None:
        _details['sortBy'] = sort_by

    if fields is not None:
        _details['fields'] = cli_util.parse_json_parameter("fields", fields)

    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.request_summarized_jre_usage(
        fleet_id=fleet_id,
        request_summarized_jre_usage_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_usage_group.command(name=cli_util.override('jms.request_summarized_managed_instance_usage.command_name', 'request-summarized'), help=u"""List managed instance usage in a specified Fleet filtered by form parameters. \n[Command Reference](requestSummarizedManagedInstanceUsage)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""The start of the time period during which resources are searched (formatted according to RFC3339). Defaults to current time minus seven days.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""The end of the time period during which resources are searched (formatted according to RFC3339). Defaults to current time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--installation-path', help=u"""The installation path of the related installation.""")
@cli_util.option('--jre-vendor', help=u"""The vendor of the related Java Runtime.""")
@cli_util.option('--jre-distribution', help=u"""The distribution of the related Java Runtime.""")
@cli_util.option('--jre-version', help=u"""The version of the related Java Runtime.""")
@cli_util.option('--application-id', help=u"""The ID of the related application.""")
@cli_util.option('--managed-instance-id', help=u"""The ID of the managed instance.""")
@cli_util.option('--managed-instance-type', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_MANAGEMENT_AGENT"]), help=u"""type of the managed instance""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeFirstSeen", "timeLastSeen", "approximateJreCount", "approximateInstallationCount", "approximateApplicationCount"]), help=u"""The field to sort managed instance views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, approximateJreCount_, _approximateInstallationCount_ and _approximateApplicationCount_  is **descending**. If no value is specified _timeLastSeen_ is default.""")
@cli_util.option('--fields', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateJreCount', 'approximateInstallationCount' and 'approximateApplicationCount'. For example 'approximateJreCount,approximateInstallationCount'.

This option is a JSON list with items of type SummarizeManagedInstanceUsageFields.  For documentation on SummarizeManagedInstanceUsageFields please see our API reference: https://docs.cloud.oracle.com/api/#/en/javamanagementservice/20210610/datatypes/SummarizeManagedInstanceUsageFields.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'jms', 'class': 'list[SummarizeManagedInstanceUsageFields]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'jms', 'class': 'list[SummarizeManagedInstanceUsageFields]'}}, output_type={'module': 'jms', 'class': 'ManagedInstanceUsageCollection'})
@cli_util.wrap_exceptions
def request_summarized_managed_instance_usage(ctx, from_json, fleet_id, time_start, time_end, installation_path, jre_vendor, jre_distribution, jre_version, application_id, managed_instance_id, managed_instance_type, sort_order, sort_by, fields, limit, page):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_start is not None:
        _details['timeStart'] = time_start

    if time_end is not None:
        _details['timeEnd'] = time_end

    if installation_path is not None:
        _details['installationPath'] = installation_path

    if jre_vendor is not None:
        _details['jreVendor'] = jre_vendor

    if jre_distribution is not None:
        _details['jreDistribution'] = jre_distribution

    if jre_version is not None:
        _details['jreVersion'] = jre_version

    if application_id is not None:
        _details['applicationId'] = application_id

    if managed_instance_id is not None:
        _details['managedInstanceId'] = managed_instance_id

    if managed_instance_type is not None:
        _details['managedInstanceType'] = managed_instance_type

    if sort_order is not None:
        _details['sortOrder'] = sort_order

    if sort_by is not None:
        _details['sortBy'] = sort_by

    if fields is not None:
        _details['fields'] = cli_util.parse_json_parameter("fields", fields)

    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.request_summarized_managed_instance_usage(
        fleet_id=fleet_id,
        request_summarized_managed_instance_usage_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_usage_group.command(name=cli_util.override('jms.summarize_application_usage.command_name', 'summarize'), help=u"""List application usage in a Fleet filtered by query parameters. \n[Command Reference](summarizeApplicationUsage)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--application-id', help=u"""The Fleet-unique identifier of the application.""")
@cli_util.option('--display-name', help=u"""The display name.""")
@cli_util.option('--application-type', help=u"""The type of the application.""")
@cli_util.option('--jre-vendor', help=u"""The vendor of the related Java Runtime.""")
@cli_util.option('--jre-distribution', help=u"""The distribution of the related Java Runtime.""")
@cli_util.option('--jre-version', help=u"""The version of the related Java Runtime.""")
@cli_util.option('--installation-path', help=u"""The file system path of the installation.""")
@cli_util.option('--managed-instance-id', help=u"""The Fleet-unique identifier of the related managed instance.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["approximateJreCount", "approximateInstallationCount", "approximateManagedInstanceCount"]), multiple=True, help=u"""Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateJreCount', 'approximateInstallationCount' and 'approximateManagedInstanceCount'. For example 'approximateJreCount,approximateInstallationCount'.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""The start of the time period during which resources are searched (formatted according to RFC3339).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""The end of the time period during which resources are searched (formatted according to RFC3339).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeFirstSeen", "timeLastSeen", "displayName", "approximateJreCount", "approximateInstallationCount", "approximateManagedInstanceCount"]), help=u"""The field to sort application views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, _approximateJreCount_, _approximateInstallationCount_ and _approximateManagedInstanceCount_  is **descending**. Default order for _displayName_ is **ascending**. If no value is specified _timeLastSeen_ is default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'ApplicationUsageCollection'})
@cli_util.wrap_exceptions
def summarize_application_usage(ctx, from_json, fleet_id, application_id, display_name, application_type, jre_vendor, jre_distribution, jre_version, installation_path, managed_instance_id, fields, time_start, time_end, limit, page, sort_order, sort_by):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if application_id is not None:
        kwargs['application_id'] = application_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if application_type is not None:
        kwargs['application_type'] = application_type
    if jre_vendor is not None:
        kwargs['jre_vendor'] = jre_vendor
    if jre_distribution is not None:
        kwargs['jre_distribution'] = jre_distribution
    if jre_version is not None:
        kwargs['jre_version'] = jre_version
    if installation_path is not None:
        kwargs['installation_path'] = installation_path
    if managed_instance_id is not None:
        kwargs['managed_instance_id'] = managed_instance_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if time_start is not None:
        kwargs['time_start'] = time_start
    if time_end is not None:
        kwargs['time_end'] = time_end
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.summarize_application_usage(
        fleet_id=fleet_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@installation_usage_group.command(name=cli_util.override('jms.summarize_installation_usage.command_name', 'summarize'), help=u"""List Java installation usage in a Fleet filtered by query parameters. \n[Command Reference](summarizeInstallationUsage)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--jre-vendor', help=u"""The vendor of the related Java Runtime.""")
@cli_util.option('--jre-distribution', help=u"""The distribution of the related Java Runtime.""")
@cli_util.option('--jre-version', help=u"""The version of the related Java Runtime.""")
@cli_util.option('--installation-path', help=u"""The file system path of the installation.""")
@cli_util.option('--application-id', help=u"""The Fleet-unique identifier of the related application.""")
@cli_util.option('--managed-instance-id', help=u"""The Fleet-unique identifier of the related managed instance.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["approximateApplicationCount", "approximateManagedInstanceCount"]), multiple=True, help=u"""Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateApplicationCount' and 'approximateManagedInstanceCount'. For example 'approximateApplicationCount,approximateManagedInstanceCount'.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""The start of the time period during which resources are searched (formatted according to RFC3339).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""The end of the time period during which resources are searched (formatted according to RFC3339).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["jreDistribution", "jreVendor", "jreVersion", "path", "timeFirstSeen", "timeLastSeen", "approximateApplicationCount", "approximateManagedInstanceCount"]), help=u"""The field to sort installation views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, and _jreVersion_, _approximateApplicationCount_ and _approximateManagedInstanceCount_  is **descending**. Default order for _jreDistribution_ and _jreVendor_ is **ascending**. If no value is specified _timeLastSeen_ is default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'InstallationUsageCollection'})
@cli_util.wrap_exceptions
def summarize_installation_usage(ctx, from_json, fleet_id, jre_vendor, jre_distribution, jre_version, installation_path, application_id, managed_instance_id, fields, time_start, time_end, limit, page, sort_order, sort_by):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if jre_vendor is not None:
        kwargs['jre_vendor'] = jre_vendor
    if jre_distribution is not None:
        kwargs['jre_distribution'] = jre_distribution
    if jre_version is not None:
        kwargs['jre_version'] = jre_version
    if installation_path is not None:
        kwargs['installation_path'] = installation_path
    if application_id is not None:
        kwargs['application_id'] = application_id
    if managed_instance_id is not None:
        kwargs['managed_instance_id'] = managed_instance_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if time_start is not None:
        kwargs['time_start'] = time_start
    if time_end is not None:
        kwargs['time_end'] = time_end
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.summarize_installation_usage(
        fleet_id=fleet_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@jre_usage_group.command(name=cli_util.override('jms.summarize_jre_usage.command_name', 'summarize'), help=u"""List Java Runtime usage in a specified Fleet filtered by query parameters. \n[Command Reference](summarizeJreUsage)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--jre-vendor', help=u"""The vendor of the Java Runtime.""")
@cli_util.option('--jre-distribution', help=u"""The distribution of the Java Runtime.""")
@cli_util.option('--jre-version', help=u"""The version of the Java Runtime.""")
@cli_util.option('--application-id', help=u"""The Fleet-unique identifier of the related application.""")
@cli_util.option('--managed-instance-id', help=u"""The Fleet-unique identifier of the related managed instance.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount"]), multiple=True, help=u"""Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateApplicationCount', 'approximateInstallationCount' and 'approximateManagedInstanceCount'. For example 'approximateApplicationCount,approximateManagedInstanceCount'.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""The start of the time period during which resources are searched (formatted according to RFC3339).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""The end of the time period during which resources are searched (formatted according to RFC3339).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["distribution", "timeFirstSeen", "timeLastSeen", "vendor", "version", "approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount"]), help=u"""The field to sort JRE usages. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, and _version_ is **descending**. Default order for _timeFirstSeen_, _timeLastSeen_, _version_, _approximateInstallationCount_, _approximateApplicationCount_ and _approximateManagedInstanceCount_  is **descending**. Default order for _distribution_ and _vendor_ is **ascending**. If no value is specified _timeLastSeen_ is default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'JreUsageCollection'})
@cli_util.wrap_exceptions
def summarize_jre_usage(ctx, from_json, fleet_id, jre_vendor, jre_distribution, jre_version, application_id, managed_instance_id, fields, time_start, time_end, limit, page, sort_order, sort_by):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if jre_vendor is not None:
        kwargs['jre_vendor'] = jre_vendor
    if jre_distribution is not None:
        kwargs['jre_distribution'] = jre_distribution
    if jre_version is not None:
        kwargs['jre_version'] = jre_version
    if application_id is not None:
        kwargs['application_id'] = application_id
    if managed_instance_id is not None:
        kwargs['managed_instance_id'] = managed_instance_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if time_start is not None:
        kwargs['time_start'] = time_start
    if time_end is not None:
        kwargs['time_end'] = time_end
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.summarize_jre_usage(
        fleet_id=fleet_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_usage_group.command(name=cli_util.override('jms.summarize_managed_instance_usage.command_name', 'summarize'), help=u"""List managed instance usage in a Fleet filtered by query parameters. \n[Command Reference](summarizeManagedInstanceUsage)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--managed-instance-id', help=u"""The Fleet-unique identifier of the managed instance.""")
@cli_util.option('--managed-instance-type', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_MANAGEMENT_AGENT"]), help=u"""The type of the managed instance.""")
@cli_util.option('--jre-vendor', help=u"""The vendor of the related Java Runtime.""")
@cli_util.option('--jre-distribution', help=u"""The distribution of the related Java Runtime.""")
@cli_util.option('--jre-version', help=u"""The version of the related Java Runtime.""")
@cli_util.option('--installation-path', help=u"""The file system path of the installation.""")
@cli_util.option('--application-id', help=u"""The Fleet-unique identifier of the related application.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["approximateJreCount", "approximateInstallationCount", "approximateApplicationCount"]), multiple=True, help=u"""Additional fields to include into the returned model on top of the required ones. This parameter can also include 'approximateJreCount', 'approximateInstallationCount' and 'approximateApplicationCount'. For example 'approximateJreCount,approximateInstallationCount'.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""The start of the time period during which resources are searched (formatted according to RFC3339).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""The end of the time period during which resources are searched (formatted according to RFC3339).""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeFirstSeen", "timeLastSeen", "approximateJreCount", "approximateInstallationCount", "approximateApplicationCount"]), help=u"""The field to sort managed instance views. Only one sort order may be provided. Default order for _timeFirstSeen_, _timeLastSeen_, approximateJreCount_, _approximateInstallationCount_ and _approximateApplicationCount_  is **descending**. If no value is specified _timeLastSeen_ is default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'jms', 'class': 'ManagedInstanceUsageCollection'})
@cli_util.wrap_exceptions
def summarize_managed_instance_usage(ctx, from_json, fleet_id, managed_instance_id, managed_instance_type, jre_vendor, jre_distribution, jre_version, installation_path, application_id, fields, time_start, time_end, limit, page, sort_order, sort_by):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')

    kwargs = {}
    if managed_instance_id is not None:
        kwargs['managed_instance_id'] = managed_instance_id
    if managed_instance_type is not None:
        kwargs['managed_instance_type'] = managed_instance_type
    if jre_vendor is not None:
        kwargs['jre_vendor'] = jre_vendor
    if jre_distribution is not None:
        kwargs['jre_distribution'] = jre_distribution
    if jre_version is not None:
        kwargs['jre_version'] = jre_version
    if installation_path is not None:
        kwargs['installation_path'] = installation_path
    if application_id is not None:
        kwargs['application_id'] = application_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if time_start is not None:
        kwargs['time_start'] = time_start
    if time_end is not None:
        kwargs['time_end'] = time_end
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.summarize_managed_instance_usage(
        fleet_id=fleet_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fleet_group.command(name=cli_util.override('jms.update_fleet.command_name', 'update'), help=u"""Update the Fleet specified by an identifier. \n[Command Reference](updateFleet)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--display-name', help=u"""The name of the Fleet. The displayName must be unique for Fleets in the same compartment.""")
@cli_util.option('--description', help=u"""The Fleet's description.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See [Understanding Free-form Tags]).""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`. (See [Managing Tags and Tag Namespaces].)""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'jms', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'jms', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'jms', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'jms', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def update_fleet(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, fleet_id, display_name, description, defined_tags, freeform_tags, if_match):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.update_fleet(
        fleet_id=fleet_id,
        update_fleet_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fleet_agent_configuration_group.command(name=cli_util.override('jms.update_fleet_agent_configuration.command_name', 'update'), help=u"""Update the Fleet Agent Configuration for the specified Fleet. \n[Command Reference](updateFleetAgentConfiguration)""")
@cli_util.option('--fleet-id', required=True, help=u"""The [OCID] of the Fleet.""")
@cli_util.option('--jre-scan-frequency-in-minutes', type=click.INT, help=u"""The frequency (in minutes) of JRE scanning. (That is, how often should JMS scan for JRE installations.)""")
@cli_util.option('--java-usage-tracker-processing-frequency-in-minutes', type=click.INT, help=u"""The frequency (in minutes) of Java Usage Tracker processing. (That is, how often should JMS process data from the Java Usage Tracker.)""")
@cli_util.option('--linux-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--windows-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the ETag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the ETag you provide matches the resource's current ETag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'linux-configuration': {'module': 'jms', 'class': 'FleetAgentOsConfiguration'}, 'windows-configuration': {'module': 'jms', 'class': 'FleetAgentOsConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'linux-configuration': {'module': 'jms', 'class': 'FleetAgentOsConfiguration'}, 'windows-configuration': {'module': 'jms', 'class': 'FleetAgentOsConfiguration'}})
@cli_util.wrap_exceptions
def update_fleet_agent_configuration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, fleet_id, jre_scan_frequency_in_minutes, java_usage_tracker_processing_frequency_in_minutes, linux_configuration, windows_configuration, if_match):

    if isinstance(fleet_id, six.string_types) and len(fleet_id.strip()) == 0:
        raise click.UsageError('Parameter --fleet-id cannot be whitespace or empty string')
    if not force:
        if linux_configuration or windows_configuration:
            if not click.confirm("WARNING: Updates to linux-configuration and windows-configuration will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if jre_scan_frequency_in_minutes is not None:
        _details['jreScanFrequencyInMinutes'] = jre_scan_frequency_in_minutes

    if java_usage_tracker_processing_frequency_in_minutes is not None:
        _details['javaUsageTrackerProcessingFrequencyInMinutes'] = java_usage_tracker_processing_frequency_in_minutes

    if linux_configuration is not None:
        _details['linuxConfiguration'] = cli_util.parse_json_parameter("linux_configuration", linux_configuration)

    if windows_configuration is not None:
        _details['windowsConfiguration'] = cli_util.parse_json_parameter("windows_configuration", windows_configuration)

    client = cli_util.build_client('jms', 'java_management_service', ctx)
    result = client.update_fleet_agent_configuration(
        fleet_id=fleet_id,
        update_fleet_agent_configuration_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
