from rest_framework import serializers
from rucio_opint_backend.apps.core.models import TransferIssue, Action, IssueCategory, Solution
from rucio_opint_backend.apps.workflow_management.models import WorkflowIssue


class TransferIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferIssue
        fields = ['id', 'message', 'src_site', 'dst_site', 'category', 'amount', 'type', 'status', 'last_modified']


class WorkflowIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowIssue
        fields = ['id', 'message', 'workflow', 'category', 'amount', 'type', 'status', 'last_modified']


class ActionSerializer(serializers.ModelSerializer):

    # TODO: Check if those two are needed
    id = serializers.ReadOnlyField()
    action = serializers.CharField(required=True)

    class Meta:
        model = Action
        fields = ['id', 'action', 'last_modified']

    # Overwriting create to implement get_or_create approach in POST requests.
    def create(self, validated_data):
        # TODO: The line below relies in the fact that validated_data['action'] is either an id or an existing Action.
        # TODO: Will break if it's neither.
        print(validated_data['action'], validated_data['action'].isdigit())
        action = validated_data['action'] if not validated_data['action'].isdigit() else Action.objects.filter(pk=validated_data['action']).first().action
        guest, created = Action.objects.get_or_create(action=action)
        return guest


# class IssueCauseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IssueCause
#         fields = ['id', 'cause', 'last_modified']


class IssueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueCategory
        fields = ['id', 'amount', 'regex', 'last_modified']


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['id', 'category', 'solution', 'propability',
                  'score', 'affected_site', 'last_modified']
